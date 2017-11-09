#include <algorithm>
#include <cctype>
#include <chrono>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

class word_cache {
  private:
	std::vector<std::string> _d;

  public:
	const std::string& operator[](std::size_t i) const {
		return _d[i];
	}
	void append(const std::string& val) {
		// Find insertion point
		auto it = std::lower_bound(_d.begin(), _d.end(), val);

		if (it != _d.end()) {
			if (*it != val) {
				_d.insert(it, val);
			}
		}
		else {
			_d.emplace_back(val);
		}
	}
	std::size_t find_element(const std::string& val) const {
		// Find insertion point
		auto it = std::lower_bound(_d.begin(), _d.end(), val);

		if (it != _d.end() && *it == val) {
			return std::distance(_d.begin(), it);
		}

		for (auto& s : _d) {
			std::cout << s << '\n';
		}

		std::cout << val << '\n';

		throw std::runtime_error("Whoops");
	}
	std::size_t size() const {
		return _d.size();
	}
};

word_cache wc;

using string_list = std::vector<std::size_t>;

string_list split(const std::string& input) {
	std::vector<std::string> tmp_output;
	std::string cache;
	for (auto c : input) {
		char lower = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
		if (('a' <= lower && lower <= 'z') || lower == '|') {
			cache.push_back(lower);
		}
		else if (cache.size() != 0) {
			wc.append(cache);
			tmp_output.emplace_back(std::move(cache));
			cache = std::string();
		}
	}

	string_list output;

	for (auto& string : tmp_output) {
		output.push_back(wc.find_element(string));
	}

	return output;
}

using markov = std::vector<std::vector<std::size_t>>;

markov build_chain(const string_list& list) {
	markov m;
	m.resize(wc.size());
	for (std::size_t i = 0; i < list.size() - 1; ++i) {
		m[list[i]].push_back(list[i + 1]);
	}
	return m;
}

int main() {
	std::ifstream f("psalms.txt");
	std::ostringstream ss;
	ss << f.rdbuf();

	auto string = ss.str();
	auto split = ::split(string);

	auto before = std::chrono::high_resolution_clock::now();
	auto mark = build_chain(split);
	auto after = std::chrono::high_resolution_clock::now();

	for (std::size_t i = 0; i < mark.size(); ++i) {
		std::cout << wc[i] << ": ";
		for (auto& word : mark[i]) {
			std::cout << " " << wc[word];
		}
		std::cout << '\n';
	}

	std::cout << (after - before).count() / 1000000.0 << "ms\n";
}

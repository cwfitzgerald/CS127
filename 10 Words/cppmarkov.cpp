#include <cctype>
#include <chrono>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

using string_list = std::vector<std::string>;

string_list split(const std::string& string);

string_list split(const std::string& string) {
	std::vector<std::string> output;
	std::string cache;
	for (auto c : string) {
		char lower = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
		if (('a' <= lower && lower <= 'z') || lower == '|') {
			cache.push_back(lower);
		}
		else if (cache.size() != 0) {
			output.emplace_back(std::move(cache));
			cache = std::string();
		}
	}

	return output;
}

using markov = std::unordered_map<std::string, std::vector<std::string>>;

markov build_chain(const string_list& list);

markov build_chain(const string_list& list) {
	markov m;
	for (std::size_t i = 0; i < list.size() - 1; ++i) {
		m[list[i]].emplace_back(list[i + 1]);
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

	for (auto const & [ key, list ] : mark) {
		std::cout << key << ": ";
		for (auto& word : list) {
			std::cout << " " << word;
		}
		std::cout << '\n';
	}

	std::cout << double((after - before).count()) / 1000000.0 << "ms\n";
}
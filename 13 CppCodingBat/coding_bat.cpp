#include <algorithm>
#include <string>
#include <utility>

std::string string_times(const std::string& input, std::uint64_t times) {
	std::string ret;
	ret.reserve(input.size() * times);
	for (std::uint64_t i = 0; i < times; ++i) {
		ret += input;
	}
	return ret;
}

std::string front_times(const std::string& input, std::uint64_t times) {
	std::string ret;
	std::size_t front_size = std::min(input.size(), static_cast<std::string::size_type>(3));
	ret.reserve(front_size * times);
	for (std::uint64_t i = 0; i < times; ++i) {
		std::copy_n(input.begin(), front_size, std::back_inserter(ret));
	}
	return ret;
}

std::string string_bits(const std::string& input) {
	std::string ret;
	ret.reserve(input.size() / 2);
	bool copy = true;
	std::copy_if(input.begin(), input.end(), std::back_inserter(ret),
	             [&copy](auto&) { return std::exchange(copy, !copy); });
	return ret;
}

std::int64_t lone_sum(std::int64_t a, std::int64_t b, std::int64_t c) {
	bool use_a = true;
	bool use_b = true;
	bool use_c = true;
	if (a == b) {
		use_a = false;
		use_b = false;
	}
	if (a == c) {
		use_a = false;
		use_c = false;
	}
	if (b == c) {
		use_b = false;
		use_c = false;
	}

	return (use_a ? a : 0) + (use_b ? b : 0) + (use_c ? c : 0);
}

std::string string_splosion(const std::string& input) {
	std::string ret;
	std::size_t output_length = (input.size() * (input.size() + 1)) / 2;
	ret.reserve(output_length);

	for (std::size_t i = 1; i < input.size(); ++i) {
		std::copy_n(input.begin(), i, std::back_inserter(ret));
	}

	return ret;
}

bool cigar_party(std::int64_t cigars, bool is_weekend) {
	return cigars >= 40 and (cigars <= 60 or is_weekend); // one case where the python code is valid c++ :)
}

int caught_speeding(double speed, bool is_birthday) {
	if (is_birthday) {
		speed -= 5;
	}

	if (speed >= 61 && speed <= 80) {
		return 1;
	}
	if (speed > 80) {
		return 2;
	}
	return 0;
}

int main() {}
#include <algorithm>
#include <iostream>
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

	for (std::size_t i = 1; i < input.size() + 1; ++i) {
		std::copy_n(input.begin(), i, std::back_inserter(ret));
	}

	return ret;
}

bool cigar_party(std::int64_t cigars, bool is_weekend) {
	return cigars >= 40 and
	       (cigars <= 60 or is_weekend); // one case where the python code is valid c++ :)
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

#define TEST_HARNESS(function, expected, ...)                                                      \
	{                                                                                              \
		auto func_out = function(__VA_ARGS__);                                                     \
		bool same = func_out == expected;                                                          \
		std::cerr << std::boolalpha << "Equal: " << same                                           \
		          << "; " #function "(" #__VA_ARGS__ ") == " << func_out                           \
		          << "; Expected == " << expected << '\n';                                         \
	}

using namespace std::string_literals;

int main() {
	TEST_HARNESS(string_times, "HiHi", "Hi", 2);
	TEST_HARNESS(string_times, "HiHiHi", "Hi", 3);
	TEST_HARNESS(string_times, "Hi", "Hi", 1);
	TEST_HARNESS(string_times, "", "Hi", 0);
	TEST_HARNESS(string_times, "HiHiHiHiHi", "Hi", 5);
	TEST_HARNESS(string_times, "Oh Boy!Oh Boy!", "Oh Boy!", 2);
	TEST_HARNESS(string_times, "xxxx", "x", 4);
	TEST_HARNESS(string_times, "", "", 4);
	TEST_HARNESS(string_times, "codecode", "code", 2);
	TEST_HARNESS(string_times, "codecodecode", "code", 3);

	TEST_HARNESS(front_times, "ChoCho", "Chocolate", 2);
	TEST_HARNESS(front_times, "ChoChoCho", "Chocolate", 3);
	TEST_HARNESS(front_times, "AbcAbcAbc", "Abc", 3);
	TEST_HARNESS(front_times, "AbAbAbAb", "Ab", 4);
	TEST_HARNESS(front_times, "AAAA", "A", 4);
	TEST_HARNESS(front_times, "", "", 4);
	TEST_HARNESS(front_times, "", "Abc", 0);

	TEST_HARNESS(string_bits, "Hlo", "Hello")
	TEST_HARNESS(string_bits, "H", "Hi")
	TEST_HARNESS(string_bits, "Hello", "Heeololeo")
	TEST_HARNESS(string_bits, "HHH", "HiHiHi")
	TEST_HARNESS(string_bits, "", "")
	TEST_HARNESS(string_bits, "Getns", "Greetings")
	TEST_HARNESS(string_bits, "Coot", "Chocoate")
	TEST_HARNESS(string_bits, "p", "pi")
	TEST_HARNESS(string_bits, "HloKte", "Hello Kitten")
	TEST_HARNESS(string_bits, "happy", "hxaxpxpxy")

	TEST_HARNESS(lone_sum, 6, 1, 2, 3)
	TEST_HARNESS(lone_sum, 2, 3, 2, 3)
	TEST_HARNESS(lone_sum, 0, 3, 3, 3)
	TEST_HARNESS(lone_sum, 9, 9, 2, 2)
	TEST_HARNESS(lone_sum, 9, 2, 2, 9)
	TEST_HARNESS(lone_sum, 9, 2, 9, 2)
	TEST_HARNESS(lone_sum, 14, 2, 9, 3)
	TEST_HARNESS(lone_sum, 9, 4, 2, 3)
	TEST_HARNESS(lone_sum, 3, 1, 3, 1)

	TEST_HARNESS(string_splosion, "CCoCodCode", "Code")
	TEST_HARNESS(string_splosion, "aababc", "abc")
	TEST_HARNESS(string_splosion, "aab", "ab")
	TEST_HARNESS(string_splosion, "x", "x")
	TEST_HARNESS(string_splosion, "ffafadfade", "fade")
	TEST_HARNESS(string_splosion, "TThTheTherThere", "There")
	TEST_HARNESS(string_splosion, "KKiKitKittKitteKitten", "Kitten")
	TEST_HARNESS(string_splosion, "BByBye", "Bye")
	TEST_HARNESS(string_splosion, "GGoGooGood", "Good")
	TEST_HARNESS(string_splosion, "BBaBad", "Bad")

	TEST_HARNESS(cigar_party, false, 30, false)
	TEST_HARNESS(cigar_party, true, 50, false)
	TEST_HARNESS(cigar_party, true, 70, true)
	TEST_HARNESS(cigar_party, false, 30, true)
	TEST_HARNESS(cigar_party, true, 50, true)
	TEST_HARNESS(cigar_party, true, 60, false)
	TEST_HARNESS(cigar_party, false, 61, false)
	TEST_HARNESS(cigar_party, true, 40, false)
	TEST_HARNESS(cigar_party, false, 39, false)
	TEST_HARNESS(cigar_party, true, 40, true)
	TEST_HARNESS(cigar_party, false, 39, true)

	TEST_HARNESS(caught_speeding, 0, 60, false)
	TEST_HARNESS(caught_speeding, 1, 65, false)
	TEST_HARNESS(caught_speeding, 0, 65, true)
	TEST_HARNESS(caught_speeding, 1, 80, false)
	TEST_HARNESS(caught_speeding, 2, 85, false)
	TEST_HARNESS(caught_speeding, 1, 85, true)
	TEST_HARNESS(caught_speeding, 1, 70, false)
	TEST_HARNESS(caught_speeding, 1, 75, false)
	TEST_HARNESS(caught_speeding, 1, 75, true)
	TEST_HARNESS(caught_speeding, 0, 40, false)
	TEST_HARNESS(caught_speeding, 0, 40, true)
	TEST_HARNESS(caught_speeding, 2, 90, false)
}

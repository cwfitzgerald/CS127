#include <iostream>
#include <string>

using namespace std::string_literals;

bool is_vowel(char c) {
	switch (c) {
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':
		case 'A':
		case 'E':
		case 'I':
		case 'O':
		case 'U':
			return true;
		default:
			return false;
	}
}

std::string piglatinify(const std::string& input) {
	if (is_vowel(input[0])) {
		return input + "ay"s;
	}
	return input.substr(1) + input[0] + "ay"s;
}

#define TEST_HARNESS(function, expected, ...)                                                                          \
	{                                                                                                                  \
		auto func_out = function(__VA_ARGS__);                                                                         \
		bool same = func_out == expected; /* NOLINT */                                                                 \
		std::cerr << std::boolalpha << (same ? "Equal: \u001b[32;1m"s : "Equal: \u001b[31;1m"s) << same                \
		          << "\u001b[0m; " << #function "(" #__VA_ARGS__ ") == " << func_out << "; Expected == " << expected   \
		          << '\n';                                                                                             \
	}

#define START_TEST(function) std::cerr << "Testing function " #function << "():\n"
#define END_TEST(function) std::cerr << "End testing function " #function << "().\n\n"

int main() {
	START_TEST(piglatinify);
	TEST_HARNESS(piglatinify, "animalay", "animal");
	TEST_HARNESS(piglatinify, "ehaviourbay", "behaviour");
	TEST_HARNESS(piglatinify, "arriagecay", "carriage");
	TEST_HARNESS(piglatinify, "evelopmentday", "development");
	TEST_HARNESS(piglatinify, "earthay", "earth");
	TEST_HARNESS(piglatinify, "amilyfay", "family");
	TEST_HARNESS(piglatinify, "overnmentgay", "government");
	TEST_HARNESS(piglatinify, "arbourhay", "harbour");
	TEST_HARNESS(piglatinify, "importantay", "important");
	TEST_HARNESS(piglatinify, "ourneyjay", "journey");
	TEST_HARNESS(piglatinify, "notkay", "knot");
	TEST_HARNESS(piglatinify, "earninglay", "learning");
	TEST_HARNESS(piglatinify, "achinemay", "machine");
	TEST_HARNESS(piglatinify, "ecessarynay", "necessary");
	TEST_HARNESS(piglatinify, "officeray", "officer");
	TEST_HARNESS(piglatinify, "aymentpay", "payment");
	TEST_HARNESS(piglatinify, "uestionqay", "question");
	TEST_HARNESS(piglatinify, "epresentativeray", "representative");
	TEST_HARNESS(piglatinify, "cissorssay", "scissors");
	TEST_HARNESS(piglatinify, "ransporttay", "transport");
	TEST_HARNESS(piglatinify, "umbrellaay", "umbrella");
	TEST_HARNESS(piglatinify, "esselvay", "vessel");
	TEST_HARNESS(piglatinify, "aterway", "water");
	TEST_HARNESS(piglatinify, "ylophonexay", "xylophone");
	TEST_HARNESS(piglatinify, "earyay", "year");
	TEST_HARNESS(piglatinify, "ebrazay", "zebra");
	END_TEST(piglatinify);
}
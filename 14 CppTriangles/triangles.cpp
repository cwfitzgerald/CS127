#include <algorithm>
#include <iostream>
#include <string>

std::string line(int l, const std::string& c) {
	std::string line;
	line.reserve(l * c.size());
	for (int i = 0; i < l; ++i) {
		std::copy(c.begin(), c.end(), std::back_inserter(line));
	}
	return line;
}

std::string rect(int w, int h) {
	std::string rect;
	rect.reserve((w + 1) * h);

	for (int row = 0; row < h; ++row) {
		std::fill_n(std::back_inserter(rect), w, '*');
		rect.push_back('\n');
	}

	return rect;
}

// clang-format off
/*
 *
 **
 ***
 ****
 */
// clang-format on
std::string tri1(int h) {
	std::string tri;
	tri.reserve((((h) * (h + 1)) / 2) + h);

	for (int i = 1; i <= h; ++i) {
		std::fill_n(std::back_inserter(tri), i, '*');
		tri.push_back('\n');
	}

	return tri;
}

// clang-format off
/*
   *
  ***
 *****
 */
// clang-format on
std::string tri2(int h) {
	std::string tri;
	auto w = h * 2 - 1;
	tri.reserve((w + 1) * h);

	for (int i = 1; i <= h; ++i) {
		auto border_width = h - i;
		std::fill_n(std::back_inserter(tri), border_width, ' ');
		std::fill_n(std::back_inserter(tri), i * 2 - 1, '*');
		std::fill_n(std::back_inserter(tri), border_width, ' ');
		tri.push_back('\n');
	}

	return tri;
}

// clang-format off
/*
  *
 **
***
 */
// clang-format on
std::string tri3(int h) {
	std::string tri;
	auto w = h;
	tri.reserve((w + 1) * h);

	for (int i = 1; i <= h; ++i) {
		auto border_width = h - i;
		std::fill_n(std::back_inserter(tri), border_width, ' ');
		std::fill_n(std::back_inserter(tri), i, '*');
		tri.push_back('\n');
	}

	return tri;
}

using namespace std::string_literals;

int main() {
	std::cout << line(15, "-"s) << '\n' << '\n';
	std::cout << rect(5, 5) << '\n';
	std::cout << tri1(5) << '\n';
	std::cout << tri2(5) << '\n';
	std::cout << tri3(5) << '\n';
}

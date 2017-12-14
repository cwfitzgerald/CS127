#include <algorithm>
#include <array>
#include <iostream>

auto paper_needed(int length, int width, int height) -> int {
	auto smallest_side = std::min(length * width, std::min(width * height, height * length));
	return 2 * length * width + 2 * width * height + 2 * height * length + smallest_side;
}

auto ribbon_needed(int length, int width, int height) -> int {
	std::array<int, 3> dimensions = {length, width, height};
	std::sort(dimensions.begin(), dimensions.end());
	return 2 * dimensions[0] + 2 * dimensions[1] + 5;
}

void test(int l, int w, int h) {
	std::cout << "Length: " << l << "in, Width: " << w << "in, Height: " << h << "in.\n\t";
	std::cout << "Paper Needed = " << paper_needed(l, w, h) << "in, "
	          << "Ribbon Needed: " << ribbon_needed(l, w, h) << "in.\n";
}

int main() {
	test(2, 3, 4);
	test(1, 8, 2);
	test(5, 5, 5);
	test(9, 2, 4);

	return 0;
}

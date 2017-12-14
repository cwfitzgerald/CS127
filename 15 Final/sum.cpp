// #include <numeric>
// sample data - you can add more
#include <iostream>
#include <type_traits>
int source_data[] = {5, 3, 19, 12, 15, 19, 33, 21, 1, 5, 26, 7, 8, 14, 18};

int sum(int* data, int size) {
	// std::accumulate(data, data + size, 0);
	int sum = 0;
	for (int i = 0; i < size; ++i) {
		sum += data[i];
	}
	return sum;
}

int sum_odd(int* data, int size) {
	// I think you've got me on this one, the accumulate thing is complicated...
	// there's no accumulate_if
	// std::accumulate(data, data + size, 0, [](int sum, int b) { return sum + (b % 2 == 1 ? b : 0) });
	int sum = 0;
	for (int i = 0; i < size; ++i) {
		if (data[i] % 2 == 1) {
			sum += data[i];
		}
	}
	return sum;
}

// Gotta return something
int main() {
	auto size = std::extent<decltype(source_data)>::value;
	std::cout << "Sum: " << sum(source_data, int(size)) << '\n';
	std::cout << "Sum Odd: " << sum_odd(source_data, int(size)) << '\n';
}
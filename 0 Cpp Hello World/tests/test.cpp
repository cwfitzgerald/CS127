#include "get_hello.hpp"
#include <gtest/gtest.h>

TEST(HelloWorldTest, ValidOutput) {
	ASSERT_STREQ(get_hello().c_str(), "Hello World!");
}

int main(int argc, char** argv) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
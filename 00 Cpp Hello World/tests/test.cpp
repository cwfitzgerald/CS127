#include "get_hello.hpp"
#include <gtest/gtest.h>

TEST(HelloWorldTest, ValidOutput) {
	ASSERT_STREQ(get_hello().c_str(), "Hello World!");
}

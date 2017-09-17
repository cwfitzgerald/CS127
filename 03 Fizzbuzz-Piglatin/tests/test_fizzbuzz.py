#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        for x in [x for x in range(0, 101, 3) if x % 5 != 0]:
            self.assertEqual(fizzbuzz.fizzbuzz(x), 'fizz')

    def test_buzz(self):
        for x in [x for x in range(0, 101, 5) if x % 3 != 0]:
            self.assertEqual(fizzbuzz.fizzbuzz(x), 'buzz')

    def test_fizzbuzz(self):
        for x in [x for x in range(0, 101, 15)]:
            self.assertEqual(fizzbuzz.fizzbuzz(x), 'fizzbuzz')

    def test_number(self):
        for x in [x for x in range(1, 101) if (x % 3 != 0 and x % 5 != 0)]:
            self.assertEqual(fizzbuzz.fizzbuzz(x), "{}".format(x))

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import comma
import random


class TestComma(unittest.TestCase):
    def test_none(self):
        self.assertEqual(comma.comma_code([]), "")

    def test_one(self):
        self.assertEqual(comma.comma_code(["hello"]), "hello")
        self.assertEqual(comma.comma_code(["Wave Hello"]), "Wave Hello")

    def test_two(self):
        self.assertEqual(comma.comma_code(["hello", "world"]), "hello and world")
        self.assertEqual(comma.comma_code(["Wave Hello", "Bleh"]), "Wave Hello and Bleh")

    def test_many(self):
        self.assertEqual(comma.comma_code(["hello", "world", "yay"]), "hello, world, and yay")
        self.assertEqual(comma.comma_code(['apples', 'bananas', 'tofu', 'cats']), "apples, bananas, tofu, and cats")
        self.assertEqual(comma.comma_code(['red', 'green', 'blue', 'orange', 'door hinge']),
                         "red, green, blue, orange, and door hinge")

if __name__ == "__main__":
    unittest.main()

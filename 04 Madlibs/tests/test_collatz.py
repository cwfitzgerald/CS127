#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import collatz
import random


class TestCollatz(unittest.TestCase):
    def test_collatz(self):
        self.assertEqual(collatz.collatz(1), 4)
        self.assertEqual(collatz.collatz(2), 1)
        self.assertEqual(collatz.collatz(3), 10)
        self.assertEqual(collatz.collatz(4), 2)
        self.assertEqual(collatz.collatz(5), 16)
        self.assertEqual(collatz.collatz(6), 3)
        self.assertEqual(collatz.collatz(7), 22)
        self.assertEqual(collatz.collatz(8), 4)
        self.assertEqual(collatz.collatz(9), 28)
        self.assertEqual(collatz.collatz(10), 5)
        self.assertEqual(collatz.collatz(11), 34)
        self.assertEqual(collatz.collatz(12), 6)
        self.assertEqual(collatz.collatz(13), 40)
        self.assertEqual(collatz.collatz(14), 7)
        self.assertEqual(collatz.collatz(15), 46)
        self.assertEqual(collatz.collatz(16), 8)
        self.assertEqual(collatz.collatz(17), 52)
        self.assertEqual(collatz.collatz(18), 9)
        self.assertEqual(collatz.collatz(19), 58)
        self.assertEqual(collatz.collatz(20), 10)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import bondify


class TestBondify(unittest.TestCase):
    def test_names(self):
        self.assertEqual(bondify.bondify("James Bond"), "Bond, James Bond")
        self.assertEqual(bondify.bondify("Connor Fitzgerald"), "Fitzgerald, Connor Fitzgerald")
        self.assertEqual(bondify.bondify("Mike Wazowski"), "Wazowski, Mike Wazowski")
        self.assertEqual(bondify.bondify("Maa'iz al-Noorani"), "al-Noorani, Maa'iz al-Noorani")

    def test_spacing(self):
        self.assertEqual(bondify.bondify("    George     Edwardson   "), "Edwardson, George Edwardson")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            bondify.bondify("JamesBond")

if __name__ == "__main__":
    unittest.main()

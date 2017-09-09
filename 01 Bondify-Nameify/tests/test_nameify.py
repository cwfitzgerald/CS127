#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import nameify


class TestNameify(unittest.TestCase):
    def test_names(self):
        self.assertEqual(nameify.nameify("james bond"), "James Bond")
        self.assertEqual(nameify.nameify("connor fitzgerald"), "Connor Fitzgerald")
        self.assertEqual(nameify.nameify("mike wazowski"), "Mike Wazowski")
        self.assertEqual(nameify.nameify("maa'iz al-Noorani"), "Maa'iz Al-Noorani")

    def test_spacing(self):
        self.assertEqual(nameify.nameify("    george     edwardson   "), "George Edwardson")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            nameify.nameify("jamesbond")

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import madlibs
import random


class TestPiglatin(unittest.TestCase):
    def setUp(self):
        random.seed(42)

    def test_single(self):
        self.assertEqual(madlibs.madlibs("NOUN"), "head")
        self.assertEqual(madlibs.madlibs("VERB"), "killed")
        self.assertEqual(madlibs.madlibs("ADJECTIVE"), "beautiful")

    def test_combo(self):
        self.assertEqual(madlibs.madlibs("Hello, I am a NOUN, and I VERB towards an ADJECTIVE thing."),
                         "Hello, I am a head, and I killed towards an beautiful thing.")

        self.assertEqual(madlibs.madlibs("Woah, a NOUN! Once, it VERB in a ADJECTIVE-ish fashion."),
                         "Woah, a table! Once, it coded in a ugly-ish fashion.")

    def test_list(self):
        self.assertEqual(madlibs.madlibs("NOUN, NOUN, NOUN, NOUN, NOUN"), "head, chair, tree, table, table")
        self.assertEqual(madlibs.madlibs("VERB, VERB, VERB, VERB, VERB"), "coded, watched, killed, watched, watched")
        self.assertEqual(madlibs.madlibs("ADJECTIVE, ADJECTIVE, ADJECTIVE, ADJECTIVE, ADJECTIVE"),
                         "old, loud, old, green, loud")

if __name__ == "__main__":
    unittest.main()

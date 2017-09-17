#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import piglatin


class TestPiglatin(unittest.TestCase):
    def test_vowel(self):
        self.assertEqual(piglatin.piglatinify("animal"), "animalay")
        self.assertEqual(piglatin.piglatinify("earth"), "earthay")
        self.assertEqual(piglatin.piglatinify("important"), "importantay")
        self.assertEqual(piglatin.piglatinify("officer"), "officeray")
        self.assertEqual(piglatin.piglatinify("umbrella"), "umbrellaay")

    def test_consonant(self):
        self.assertEqual(piglatin.piglatinify("behaviour"), "ehaviourbay")
        self.assertEqual(piglatin.piglatinify("carriage"), "arriagecay")
        self.assertEqual(piglatin.piglatinify("development"), "evelopmentday")
        self.assertEqual(piglatin.piglatinify("family"), "amilyfay")
        self.assertEqual(piglatin.piglatinify("government"), "overnmentgay")
        self.assertEqual(piglatin.piglatinify("harbour"), "arbourhay")
        self.assertEqual(piglatin.piglatinify("journey"), "ourneyjay")
        self.assertEqual(piglatin.piglatinify("knot"), "notkay")
        self.assertEqual(piglatin.piglatinify("learning"), "earninglay")
        self.assertEqual(piglatin.piglatinify("machine"), "achinemay")
        self.assertEqual(piglatin.piglatinify("necessary"), "ecessarynay")
        self.assertEqual(piglatin.piglatinify("payment"), "aymentpay")
        self.assertEqual(piglatin.piglatinify("question"), "uestionqay")
        self.assertEqual(piglatin.piglatinify("representative"), "epresentativeray")
        self.assertEqual(piglatin.piglatinify("scissors"), "cissorssay")
        self.assertEqual(piglatin.piglatinify("transport"), "ransporttay")
        self.assertEqual(piglatin.piglatinify("vessel"), "esselvay")
        self.assertEqual(piglatin.piglatinify("water"), "aterway")
        self.assertEqual(piglatin.piglatinify("xylophone"), "ylophonexay")
        self.assertEqual(piglatin.piglatinify("year"), "earyay")
        self.assertEqual(piglatin.piglatinify("zebra"), "ebrazay")

if __name__ == "__main__":
    unittest.main()

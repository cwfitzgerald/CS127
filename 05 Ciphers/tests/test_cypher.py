#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import cypher
import random


class TestCypher(unittest.TestCase):
    def test_encode_letter_distances(self):
        self.assertEqual(cypher.encode_letter('a', 0), 'a')
        self.assertEqual(cypher.encode_letter('a', 1), 'b')
        self.assertEqual(cypher.encode_letter('a', 2), 'c')
        self.assertEqual(cypher.encode_letter('a', 3), 'd')
        self.assertEqual(cypher.encode_letter('a', 4), 'e')
        self.assertEqual(cypher.encode_letter('a', 5), 'f')
        self.assertEqual(cypher.encode_letter('a', 6), 'g')
        self.assertEqual(cypher.encode_letter('a', 7), 'h')
        self.assertEqual(cypher.encode_letter('a', 8), 'i')
        self.assertEqual(cypher.encode_letter('a', 9), 'j')
        self.assertEqual(cypher.encode_letter('a', 10), 'k')
        self.assertEqual(cypher.encode_letter('a', 11), 'l')
        self.assertEqual(cypher.encode_letter('a', 12), 'm')
        self.assertEqual(cypher.encode_letter('a', 13), 'n')
        self.assertEqual(cypher.encode_letter('a', 14), 'o')
        self.assertEqual(cypher.encode_letter('a', 15), 'p')
        self.assertEqual(cypher.encode_letter('a', 16), 'q')
        self.assertEqual(cypher.encode_letter('a', 17), 'r')
        self.assertEqual(cypher.encode_letter('a', 18), 's')
        self.assertEqual(cypher.encode_letter('a', 19), 't')
        self.assertEqual(cypher.encode_letter('a', 20), 'u')
        self.assertEqual(cypher.encode_letter('a', 21), 'v')
        self.assertEqual(cypher.encode_letter('a', 22), 'w')
        self.assertEqual(cypher.encode_letter('a', 23), 'x')
        self.assertEqual(cypher.encode_letter('a', 24), 'y')
        self.assertEqual(cypher.encode_letter('a', 25), 'z')
        self.assertEqual(cypher.encode_letter('a', 26), 'a')

    def test_encode_letter_starting(self):
        self.assertEqual(cypher.encode_letter('a', 1), 'b')
        self.assertEqual(cypher.encode_letter('b', 1), 'c')
        self.assertEqual(cypher.encode_letter('c', 1), 'd')
        self.assertEqual(cypher.encode_letter('d', 1), 'e')
        self.assertEqual(cypher.encode_letter('e', 1), 'f')
        self.assertEqual(cypher.encode_letter('f', 1), 'g')
        self.assertEqual(cypher.encode_letter('g', 1), 'h')
        self.assertEqual(cypher.encode_letter('h', 1), 'i')
        self.assertEqual(cypher.encode_letter('i', 1), 'j')
        self.assertEqual(cypher.encode_letter('j', 1), 'k')
        self.assertEqual(cypher.encode_letter('k', 1), 'l')
        self.assertEqual(cypher.encode_letter('l', 1), 'm')
        self.assertEqual(cypher.encode_letter('m', 1), 'n')
        self.assertEqual(cypher.encode_letter('n', 1), 'o')
        self.assertEqual(cypher.encode_letter('o', 1), 'p')
        self.assertEqual(cypher.encode_letter('p', 1), 'q')
        self.assertEqual(cypher.encode_letter('q', 1), 'r')
        self.assertEqual(cypher.encode_letter('r', 1), 's')
        self.assertEqual(cypher.encode_letter('s', 1), 't')
        self.assertEqual(cypher.encode_letter('t', 1), 'u')
        self.assertEqual(cypher.encode_letter('u', 1), 'v')
        self.assertEqual(cypher.encode_letter('v', 1), 'w')
        self.assertEqual(cypher.encode_letter('w', 1), 'x')
        self.assertEqual(cypher.encode_letter('x', 1), 'y')
        self.assertEqual(cypher.encode_letter('y', 1), 'z')
        self.assertEqual(cypher.encode_letter('z', 1), 'a')

    def test_encode_string(self):
        self.assertEqual(cypher.encode_string('hello world!', 2), "jgnnq yqtnf!")

    def test_encode_string_ignore_other_characters(self):
        self.assertEqual(cypher.encode_string('hello world!^^23A&*^@', 26), 'hello world!^^23A&*^@')

    def test_full_encode(self):
        result = """hello world!
ifmmp xpsme!
jgnnq yqtnf!
khoor zruog!
lipps asvph!
mjqqt btwqi!
nkrru cuxrj!
olssv dvysk!
pmttw ewztl!
qnuux fxaum!
rovvy gybvn!
spwwz hzcwo!
tqxxa iadxp!
uryyb jbeyq!
vszzc kcfzr!
wtaad ldgas!
xubbe mehbt!
yvccf nficu!
zwddg ogjdv!
axeeh phkew!
byffi qilfx!
czggj rjmgy!
dahhk sknhz!
ebiil tloia!
fcjjm umpjb!
gdkkn vnqkc!"""
        self.assertEqual(cypher.full_encode('hello world!'), result)

if __name__ == "__main__":
    unittest.main()

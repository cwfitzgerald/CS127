#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import cb


class TestCB(unittest.TestCase):
    def test_string_times(self):
        self.assertEqual(cb.string_times('Hi', 2), 'HiHi')
        self.assertEqual(cb.string_times('Hi', 3), 'HiHiHi')
        self.assertEqual(cb.string_times('Hi', 1), 'Hi')
        self.assertEqual(cb.string_times('Hi', 0), '')
        self.assertEqual(cb.string_times('Hi', 5), 'HiHiHiHiHi')
        self.assertEqual(cb.string_times('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
        self.assertEqual(cb.string_times('x', 4), 'xxxx')
        self.assertEqual(cb.string_times('', 4), '')
        self.assertEqual(cb.string_times('code', 2), 'codecode')
        self.assertEqual(cb.string_times('code', 3), 'codecodecode')

    def test_front_times(self):
        self.assertEqual(cb.front_times('Chocolate', 2), 'ChoCho')
        self.assertEqual(cb.front_times('Chocolate', 3), 'ChoChoCho')
        self.assertEqual(cb.front_times('Abc', 3), 'AbcAbcAbc')
        self.assertEqual(cb.front_times('Ab', 4), 'AbAbAbAb')
        self.assertEqual(cb.front_times('A', 4), 'AAAA')
        self.assertEqual(cb.front_times('', 4), '')
        self.assertEqual(cb.front_times('Abc', 0), '')

    def test_string_bits(self):
        self.assertEqual(cb.string_bits('Hello'), 'Hlo')
        self.assertEqual(cb.string_bits('Hi'), 'H')
        self.assertEqual(cb.string_bits('Heeololeo'), 'Hello')
        self.assertEqual(cb.string_bits('HiHiHi'), 'HHH')
        self.assertEqual(cb.string_bits(''), '')
        self.assertEqual(cb.string_bits('Greetings'), 'Getns')
        self.assertEqual(cb.string_bits('Chocoate'), 'Coot')
        self.assertEqual(cb.string_bits('pi'), 'p')
        self.assertEqual(cb.string_bits('Hello Kitten'), 'HloKte')
        self.assertEqual(cb.string_bits('hxaxpxpxy'), 'happy')

    def test_lone_sum(self):
        self.assertEqual(cb.lone_sum(1, 2, 3), 6)
        self.assertEqual(cb.lone_sum(3, 2, 3), 2)
        self.assertEqual(cb.lone_sum(3, 3, 3), 0)
        self.assertEqual(cb.lone_sum(9, 2, 2), 9)
        self.assertEqual(cb.lone_sum(2, 2, 9), 9)
        self.assertEqual(cb.lone_sum(2, 9, 2), 9)
        self.assertEqual(cb.lone_sum(2, 9, 3), 14)
        self.assertEqual(cb.lone_sum(4, 2, 3), 9)
        self.assertEqual(cb.lone_sum(1, 3, 1), 3)

    def test_string_splosion(self):
        self.assertEqual(cb.string_splosion('Code'), 'CCoCodCode')
        self.assertEqual(cb.string_splosion('abc'), 'aababc')
        self.assertEqual(cb.string_splosion('ab'), 'aab')
        self.assertEqual(cb.string_splosion('x'), 'x')
        self.assertEqual(cb.string_splosion('fade'), 'ffafadfade')
        self.assertEqual(cb.string_splosion('There'), 'TThTheTherThere')
        self.assertEqual(cb.string_splosion('Kitten'), 'KKiKitKittKitteKitten')
        self.assertEqual(cb.string_splosion('Bye'), 'BByBye')
        self.assertEqual(cb.string_splosion('Good'), 'GGoGooGood')
        self.assertEqual(cb.string_splosion('Bad'), 'BBaBad')

    def test_cigar_party(self):
        self.assertEqual(cb.cigar_party(30, False), False)
        self.assertEqual(cb.cigar_party(50, False), True)
        self.assertEqual(cb.cigar_party(70, True), True)
        self.assertEqual(cb.cigar_party(30, True), False)
        self.assertEqual(cb.cigar_party(50, True), True)
        self.assertEqual(cb.cigar_party(60, False), True)
        self.assertEqual(cb.cigar_party(61, False), False)
        self.assertEqual(cb.cigar_party(40, False), True)
        self.assertEqual(cb.cigar_party(39, False), False)
        self.assertEqual(cb.cigar_party(40, True), True)
        self.assertEqual(cb.cigar_party(39, True), False)

    def test_caught_speeding(self):
        self.assertEqual(cb.caught_speeding(60, False), 0)
        self.assertEqual(cb.caught_speeding(65, False), 1)
        self.assertEqual(cb.caught_speeding(65, True), 0)
        self.assertEqual(cb.caught_speeding(80, False), 1)
        self.assertEqual(cb.caught_speeding(85, False), 2)
        self.assertEqual(cb.caught_speeding(85, True), 1)
        self.assertEqual(cb.caught_speeding(70, False), 1)
        self.assertEqual(cb.caught_speeding(75, False), 1)
        self.assertEqual(cb.caught_speeding(75, True), 1)
        self.assertEqual(cb.caught_speeding(40, False), 0)
        self.assertEqual(cb.caught_speeding(40, True), 0)
        self.assertEqual(cb.caught_speeding(90, False), 2)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import picture
import random


class TestCreateMatrix(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(picture.create_matrix(0, 0), [])

    def test_square(self):
        self.assertEqual(picture.create_matrix(2, 2), [['', ''],
                                                       ['', '']])

    def test_rectangle(self):
        self.assertEqual(picture.create_matrix(3, 2), [['', ''],
                                                       ['', ''],
                                                       ['', '']])


class TestConsistant(unittest.TestCase):
    def test_empty(self):
        empty_matrix = []
        self.assertEqual(picture.matrix_consistant(empty_matrix), True)

    def test_varying_rows(self):
        start = [['a', 'b'],
                 ['c', 'd', 'e']]

        self.assertEqual(picture.matrix_consistant(start), False)

    def test_square(self):
        start = [['a', 'b'],
                 ['c', 'd']]

        self.assertEqual(picture.matrix_consistant(start), True)

    def test_rectangle(self):
        start = [['a', 'b', 'c'],
                 ['d', 'e', 'f']]

        self.assertEqual(picture.matrix_consistant(start), True)


class TestTranspose(unittest.TestCase):
    def test_empty(self):
        empty_matrix = []
        self.assertEqual(picture.matrix_transpose(empty_matrix), empty_matrix)

    def test_square(self):
        start = [['a', 'b'],
                 ['c', 'd']]
        end = [['a', 'c'],
               ['b', 'd']]

        self.assertEqual(picture.matrix_transpose(start), end)

    def test_rectangle(self):
        start = [['a', 'b', 'c'],
                 ['d', 'e', 'f']]
        end = [['a', 'd'],
               ['b', 'e'],
               ['c', 'f']]

        self.assertEqual(picture.matrix_transpose(start), end)

    def test_sample(self):
        start = [['.', '.', '.', '.', '.', '.'],
                 ['.', 'O', 'O', '.', '.', '.'],
                 ['O', 'O', 'O', 'O', '.', '.'],
                 ['O', 'O', 'O', 'O', 'O', '.'],
                 ['.', 'O', 'O', 'O', 'O', 'O'],
                 ['O', 'O', 'O', 'O', 'O', '.'],
                 ['O', 'O', 'O', 'O', '.', '.'],
                 ['.', 'O', 'O', '.', '.', '.'],
                 ['.', '.', '.', '.', '.', '.']]
        end = [['.', '.', 'O', 'O', '.', 'O', 'O', '.', '.'],
               ['.', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '.'],
               ['.', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '.'],
               ['.', '.', 'O', 'O', 'O', 'O', 'O', '.', '.'],
               ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],
               ['.', '.', '.', '.', 'O', '.', '.', '.', '.']]

        self.assertEqual(picture.matrix_transpose(start), end)

if __name__ == "__main__":
    unittest.main()

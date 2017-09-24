#!/usr/bin/env python3

# Very clever... this is just matrix transposition

import typing


def create_matrix(x: int, y: int) -> typing.List[typing.List[str]]:
    """Create 2D array of size (x, y)"""
    return [['' for _ in range(y)] for _ in range(x)]


def matrix_consistant(matrix: typing.List[typing.List[str]]) -> bool:
    """Check if all rows have the same length within 2D array"""
    if len(matrix) == 0:
        return True

    first_len = len(matrix[0])

    return all([len(col) == first_len for col in matrix])


def matrix_transpose(matrix: typing.List[typing.List[str]]) -> typing.List[typing.List[str]]:
    """Rotate 2D array clockwise"""
    if len(matrix) == 0:
        return []

    if not matrix_consistant(matrix):
        raise ValueError("Matrix row lengths inconsistant.")

    x_size = len(matrix)
    y_size = len(matrix[0])

    new_matrix = create_matrix(y_size, x_size)

    for x in range(x_size):
        for y in range(y_size):
            new_matrix[y][x] = matrix[x][y]

    return new_matrix


def print_matrix(matrix: typing.List[typing.List[str]]) -> None:
    for row in matrix:
        print("".join(row))

if __name__ == "__main__":
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    print_matrix(grid)
    print(matrix_transpose(grid))

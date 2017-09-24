#!/usr/bin/env python3

import typing


def collatz(num: int) -> int:
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1


if __name__ == "__main__":
    while (True):
        num = input("Enter Number:\n> ")
        val = 0

        try:
            val = int(num)
        except ValueError as E:
            print("Try again.")
            continue

        while val != 1:
            val = collatz(val)
            print val

#!/usr/bin/env python3

# I added an autosolving cypher solver in cypher_solver.py

import typing


def encode_letter(letter: str, amount: int) -> str:
    '''Apply an rot<amount> cypher on the input letter'''
    amount = amount % 26

    letter = ord(letter)
    if letter >= 65 and letter <= 90:
        letter = ((letter - 65 + amount) % 26) + 65
    elif letter >= 97 and letter <= 122:
        letter = ((letter - 97 + amount) % 26) + 97
    return chr(letter)


def encode_string(string: str, amount: int) -> str:
    '''Apply an rot<amount> cypher on the input string'''
    return "".join([encode_letter(c, amount) for c in string])


def full_encode(cyphertext: str) -> str:
    '''Apply an rot0 - rot25 cypher on the input string'''
    return "\n".join([encode_string(cyphertext, x) for x in range(0, 26)])

if __name__ == '__main__':
    while (True):
        print(full_encode(input("Enter Text:\n> ")))

#!/usr/bin/env python3

import math
import operator
import os

# Cypher Code


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
    return [encode_string(cyphertext, x) for x in range(0, 26)]


# Resolution Code

def generate_english_frequencies():
    filepath = os.path.join(os.path.dirname(__file__), "complete_works_of_william_shakespeare.dat")
    with open(filepath, "r") as f:
        full_string = f.read()
        return build_frequency_vector(full_string)


def min_index(l):
    return min(range(len(l)), key=l.__getitem__)


def max_index(l):
    return max(range(len(l)), key=l.__getitem__)


def distance(l1, l2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(l1, l2)]))


def build_frequency_vector(string):
    filtered = (c.lower() for c in string
                if ((ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122)))

    frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    size = 0
    for c in filtered:
        frequency[(ord(c) - 97)] += 1
        size += 1

    frequency = [f / size for f in frequency]

    return frequency


english_letter_frequencies = None


def decode(string):
    global english_letter_frequencies

    if english_letter_frequencies is None:
        english_letter_frequencies = generate_english_frequencies()
    rotations = full_encode(string)
    frequencies = [build_frequency_vector(r) for r in rotations]
    minimum = min_index([distance(f, english_letter_frequencies) for f in frequencies])

    return rotations[minimum]


if __name__ == "__main__":
    print(decode("Xubbe, xem qhu oek teydw jetqo? Y qc xqlydw qd qriebkjbo medtuhvkb tqo, qdt Y xefu oek mybb jee"))
    print(english_letter_frequencies)

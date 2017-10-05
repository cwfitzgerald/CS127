#!/usr/bin/env python3

import math
import operator

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

letter_frequencies = [0.08167,  # A
                      0.01492,  # B
                      0.02782,  # C
                      0.04253,  # D
                      0.12702,  # E
                      0.02228,  # F
                      0.02015,  # G
                      0.06094,  # H
                      0.06966,  # I
                      0.00153,  # J
                      0.00772,  # K
                      0.04025,  # L
                      0.02406,  # M
                      0.06749,  # N
                      0.07507,  # O
                      0.01929,  # P
                      0.00095,  # Q
                      0.05987,  # R
                      0.06327,  # S
                      0.09056,  # T
                      0.02758,  # U
                      0.00978,  # V
                      0.02360,  # W
                      0.00150,  # X
                      0.01974,  # Y
                      0.00074]  # Z


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


def decode(string):
    rotations = full_encode(string)
    frequencies = [build_frequency_vector(r) for r in rotations]
    minimum = min_index([distance(f, letter_frequencies) for f in frequencies])

    return rotations[minimum]


if __name__ == "__main__":
    # print(distance(build_frequency_vector("I am going to write a sentence that is much more well suited"
    #                                       "for what a normal sentence looks like"), letter_frequencies))

    print(decode("Xubbe, xem qhu oek teydw jetqo? Y qc xqlydw qd qriebkjbo medtuhvkb tqo, qdt Y xefu oek mybb jee"))

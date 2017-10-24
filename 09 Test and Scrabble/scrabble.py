#!/usr/bin/env python3


scorelist = [1,   # A
             3,   # B
             3,   # C
             2,   # D
             1,   # E
             4,   # F
             2,   # G
             4,   # H
             1,   # I
             8,   # J
             5,   # K
             1,   # L
             3,   # M
             1,   # N
             1,   # O
             3,   # P
             10,  # Q
             1,   # R
             1,   # S
             1,   # T
             1,   # U
             4,   # V
             4,   # W
             8,   # X
             4,   # Y
             10,  # Z
             ]


def score(string):
    return sum([scorelist[ord(c) - ord('a')] for c in string.lower() if 'a' <= c and c <= 'z'])

if __name__ == "__main__":
    print(score("hello"))                                       # 8
    print(score("antidisestablishmentarianism"))                # 3
    print(score("valid"))                                       # 9
    print(score("The quick red fox jumped over the lazy dog"))  # Crash Test - All Letters and Spaces

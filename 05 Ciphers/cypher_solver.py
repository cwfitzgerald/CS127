#!/usr/bin/env python3

import collections
import cypher  # Name of rotation cypher implimentation
import itertools
import math
import sys
import typing

# Alias for the type used for dictionary
Dictionary = typing.Dict[int, typing.List[str]]

verbose = False


def load_dictfile() -> Dictionary:
    with open("/usr/share/dict/words", "r") as file:
        values = {}
        for line in file:
            line = line.strip()
            line = line.lower()
            length = len(line)
            if length not in values:
                values[length] = []
            values[length].append(line)
        return values


def letter_distance(word1: str, word2: str) -> typing.List[int]:
    distances = []
    for c1, c2 in zip(word1, word2):
        diff = ord(c2) - ord(c1)
        if (diff < 0):
            diff += 26
        distances.append(diff)

    return distances


def consistant_distance(word1: str, word2: str) -> typing.Tuple[bool, int]:
    distance = letter_distance(word1, word2)

    return (all([d == distance[0] for d in distance]), distance[0])


def dictionary_distance(dictionary: Dictionary, word: str) -> typing.List[int]:
    matches = []

    word = word.lower()

    word = "".join([c for c in word if ((ord(c) >= 97 and ord(c) <= 122) or ord(c) == 39)])

    for dict_word in dictionary[len(word)]:
        dist = consistant_distance(word, dict_word)
        if dist[0]:
            matches.append((dict_word, dist[1]))

    return matches


def autodecode_string(dictionary: Dictionary, string: str) -> str:
    global verbose

    separated = string.split()

    possible_distances = [dictionary_distance(dictionary, w) for w in separated]

    if verbose:
        print("\nPer-Word Matches:\nWord\t\tRotation\tNew Word")
        for word, pd in zip(separated, possible_distances):
            if not isinstance(pd, list):
                pd = [pd]

            print("\n".join(["{} {}Rot{}\t\t\"{}\"".format(word,
                                                           '\t' * int(math.ceil((15 - len(word)) / 8)),
                                                           p[1],
                                                           p[0])
                             for p in pd]))

    distance_counts = collections.Counter([x[1] for x in itertools.chain.from_iterable(possible_distances)])

    if verbose:
        print("\nCommon Rotations:")
        for offset, count in distance_counts.items():
            print("{} word{} Rot{}".format(count, 's match  ' if count > 1 else '  matches', offset))

    if (len(distance_counts) == 0):
        if verbose:
            print("No Matches Found\n\nChoosing Rot0")

        return [(0, string)]

    common = distance_counts.most_common(26)

    total_results = 0
    for x in common:
        if x == common[0]:
            total_results += 1

    result = []

    for i in range(total_results):
        result.append((common[i][0], cypher.encode_string(string, common[i][0])))

    if verbose:
        print('')
        for offset, _ in result:
            print("Choosing Rot{}".format(offset))

    return result


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == '-v':
        verbose = True

    dictionary = load_dictfile()
    while (True):
        results = autodecode_string(dictionary, input("Enter Text:\n> "))

        print("\nAnswer{}:".format('s' if len(results) > 2 else ''))
        for r in results:
            print("Rot{}: {}\n".format(r[0], r[1]))

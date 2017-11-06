#!/usr/bin/env python3

import collections
import os


def remove_nonalpha(w):
    '''
    input: w - string-like represeting a word
    output: string with non alpha chars removed
    '''
    return "".join([l for l in w if l.isalpha()])


def count_words(wordlist):
    '''
    input: wordlist - list-likes holding string-likes respresenting a list of words
    output: dictionary with word as key and count as value
    '''
    d = collections.defaultdict(lambda: 0)
    for w in wordlist:
        d[w] += 1
    return dict(d)


def count_words_in_file(name):
    '''
    intput: name - string-like representing filename to count the words of
    output: dictionary with word as key and count as value
    '''

    # Get filename relative to module location
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), name)

    with open(filename) as file:
        text = file.read()
        list_of_words = [remove_nonalpha(w.lower()) for w in text.split()]
        word_count = count_words(list_of_words)
        return word_count


def create_markov_chain(list_of_words):
    dict = collections.defaultdict(lambda: [])

    for i in range(0, len(list_of_words) - 1):
        dict[list_of_words[i]].append(list_of_words[i + 1])

    return dict


def create_markov_chain_from_file(name):
    # Get filename relative to module location
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), name)

    with open(filename) as file:
        text = file.read()
        return create_markov_chain([remove_nonalpha(w) for w in text.split()])


if __name__ == "__main__":
    d = create_markov_chain_from_file("hamlet.txt")
    print(d)

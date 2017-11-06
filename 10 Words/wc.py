#!/usr/bin/env python3

import collections
import os
import pprint


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
    '''
    input: list_of_words - list-like of string-like representing a list of words in order used
    output: dictionary with the word as key and list of possible next words as value
    '''
    d = collections.defaultdict(lambda: [])

    for i in range(0, len(list_of_words) - 1):
        d[list_of_words[i]].append(list_of_words[i + 1])

    return dict(d)


def create_markov_chain_from_file(name):
    '''
    input: name - filename to create markov chain from
    output: dictionary with the word as key and list of possible next words as value
    '''
    # Get filename relative to module location
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), name)

    with open(filename) as file:
        text = file.read().lower()
        return create_markov_chain([remove_nonalpha(w) for w in text.split()])


if __name__ == "__main__":
    d = create_markov_chain_from_file("psalms.txt")
    pprint.pprint(d)

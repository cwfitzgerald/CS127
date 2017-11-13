#!/usr/bin/env python3

import collections
import os
import random
import pprint


def remove_nonalpha(w):
    '''
    input: w - string-like represeting a word
    output: string with non alpha chars removed
    '''
    return "".join([l for l in w if l.isalpha()])


def create_markov_chain(list_of_words, depth):
    '''
     input: list_of_words - list-like of string-like representing a list of words in order used
           depth         - markov chain depth to use. 3 = key of three words in a tuple
    output: dictionary with the word as key and list of possible next words as value
    '''
    result = collections.defaultdict(lambda: [])

    for i in range(0, len(list_of_words) - 1):
        for d in range(0, depth):
            result[tuple(list_of_words[max(0, i - d):i + 1])].append(list_of_words[i + 1])

    # Words are all lowercase, uppercase keys are for details about the dict
    result["DEPTH"] = depth

    return dict(result)


def create_markov_chain_from_file(name, depth):
    '''
    i nput:  name - filename to create markov chain from
            depth - markov chain depth to use. 3 = key of three words in a tuple
    output: dictionary with the words as key and list of possible next words as value
    '''
    # Get filename relative to module location
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), name)

    with open(filename) as file:
        text = file.read().lower()
        return create_markov_chain([remove_nonalpha(w) for w in text.split()], depth)


def build_sentence_from_chain(dictionary, start_word, length=50):
    '''
     input: dictionary - markov chain dictionary to generate sentence from
            start_word - single word to start the sentence with
            length     - length of sentence to generate
    output: string-like with generated sentence
    '''
    depth = dictionary["DEPTH"]  # Get depth from dictionary

    start_word = start_word.lower()  # All keys are lower case

    t = (start_word,)  # Start with a tuple with just the start word

    output = [start_word]  # The output always starts with the start word

    # Need (length - 1) words
    for i in range(length - 1):
        # If a full tuple isn't found, keep shortening the tuple to find a
        # more generic chain to go off of
        # Ex.
        # ("hello", "my", "name") -> KeyError
        # ("my", "name") -> KeyError
        # ("name",) -> KeyError
        # (,) -> Nothing found to continue chain, abort
        for attempt in range(0, depth):
            try:
                new_word = random.choice(dictionary[t[attempt:]])
                break
            except KeyError:
                # Keep going if this is not the last attempt
                if attempt != depth - 1:
                    continue
                # Kill the program if the chain is dead
                else:
                    raise KeyError("Dead end in markov chain")

        # Add the found word to output
        output.append(new_word)
        # If the tuple isn't at full chain length, add more
        if (len(t) < depth):
            t = (*t, new_word)
        # If the tuple is at max length, chop off the first word then add another
        else:
            t = (*t[1:], new_word)

    # Return a joined output for prettiness's sake
    return " ".join(output)


if __name__ == "__main__":
    d = create_markov_chain_from_file("psalms.txt", 3)
    # pprint.pprint(d)
    print(build_sentence_from_chain(d, "I"))

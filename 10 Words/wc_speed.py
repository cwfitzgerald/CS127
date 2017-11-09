#!/usr/bin/env python3

import wc
import timeit


with open("psalms.txt") as f:
    array = f.read().lower().split()

print(timeit.timeit("wc.create_markov_chain(array)", number=1000, globals=globals()), "ms")
print(timeit.timeit("wc.sort_words(array)", number=1000, globals=globals()), "ms")

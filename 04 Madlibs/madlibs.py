import random
import re

story = """ There once was a NOUN who VERB. He was very ADJECTIVE. He VERB very well.   """
nouns = ["chair", "head", "desk", "table", "tree", "paper", "towel", "file"]
verbs = ["kill", "coded", "ran", "jumping", "swim", "watch", "existed"]
adjectives = ["loud", "ugly", "beautiful", "green", "old"]
keywords = ["NOUN", "VERB", "ADJECTIVE"]


def convert(word):
    global nouns, verbs, adjectives
    print(word)
    if "NOUN" == word:
        return random.choice(nouns)
    elif "VERB" == word:
        return random.choice(verbs)
    elif "ADJECTIVE" == word:
        return random.choice(adjectives)
    else:
        return word


def madlibs():
    global story

    orig = story.strip()

    result = re.finditer(r'NOUN|VERB|ADJECTIVE', orig)

    s = ""

    for x in result:
        span = x.span()
        new = convert(orig[span[0]:span[1]])
        s = orig[0:span[0]] + new + orig[span[1]:]

    return s

if __name__ == "__main__":
    print(madlibs())

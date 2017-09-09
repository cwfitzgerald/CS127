#!/usr/bin/env python3


def nameify(string):
    string = string.strip()
    space_location = string.find(' ')

    if space_location == -1:
        raise ValueError("No split in string")

    first = string[0:space_location]
    last = string[space_location + 1:]

    first = first.strip()
    last = last.strip()

    first = first[0].upper() + first[1:]
    last = last[0].upper() + last[1:]

    bonded = first + " " + last

    return bonded


if __name__ == "__main__":
    string = "hello world"
    string2 = string.title()   # is this what you want?
    string3 = nameify(string)  # or this?
    string4 = "Hello World"    # or this?

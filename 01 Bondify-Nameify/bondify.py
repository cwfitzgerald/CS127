#!/usr/bin/env python3


def bondify(string):
    string = string.strip()

    space_location = string.find(' ')

    if space_location == -1:
        raise ValueError("Name must have two names in it")

    first = string[0:space_location]
    last = string[space_location + 1:]

    first = first.strip()
    last = last.strip()

    bonded = last + ", " + first + " " + last

    return bonded

if __name__ == "__main__":
    st = "James Bond"
    bond = bondify(st)
    print(st + " -> " + bond)
    if bond == "Bond, James Bond":
        print("Sucess!")

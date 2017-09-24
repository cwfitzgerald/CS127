#!/usr/bin/env python3


def piglatinify(string: str) -> str:
    string = string.strip()

    if len(string) == 0:
        raise ValueError("String of size zero")

    if string[0] not in "aeiou":
        string = string[1:] + string[0]

    string += "ay"

    return string

if __name__ == "__main__":
    print(piglatinify("latin"))
    print(piglatinify("amish"))

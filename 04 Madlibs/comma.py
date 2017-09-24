#!/usr/bin/env python3

import typing


def comma_code(in_list: typing.List[str]) -> str:
    length = len(in_list)

    if length == 0:
        return ""
    elif length == 1:
        return in_list[0]
    elif length == 2:
        return " and ".join(in_list)
    else:
        return ", ".join(in_list[0:-1]) + ", and " + in_list[-1]

if __name__ == "__main__":
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(spam)
    print(comma_code(spam))

#!/usr/bin/env python3


def encode(string):
    if len(string) == 0:
        return []
    if len(string) == 1:
        return [string]

    result = []

    curval = string[0]
    curcount = 1

    for c in string[1:]:
        if c == curval:
            curcount += 1
        else:
            if curcount != 1:  # Lets actually solve the problem correctly this time
                result.append(curcount)
            result.append(curval)
            curval = c
            curcount = 1

    if curcount != 1:  # Lets actually solve the problem correctly this time
        result.append(curcount)
    result.append(curval)

    return result


if __name__ == "__main__":
    print(encode(""))                # []
    print(encode("a"))               # ['a']
    print(encode("aaaaa"))           # [5, 'a']
    print(encode("aabba"))           # [2, 'a', 2, 'b', 'a']
    print(encode("😊😊😊😊"))         # [3, '😊']
    print(encode("aabcccdeeeeaaa"))  # [2, 'a', 'b', 3, 'c', d, 4, 'e', 3, 'a']

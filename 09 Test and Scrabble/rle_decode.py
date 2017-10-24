#!/usr/bin/env python3


def rle_decode(l):
    # This parser is stateful because there's no idiomatic way (that I know of)
    # to properly act as if you have a single mutable index variable
    # *shrug*

    grab_char = False
    length = 1

    result = []

    for e in l:
        if grab_char:
            for i in range(length):
                result.append(e)
            grab_char = False
        else:
            if isinstance(e, str):
                result.append(e)
            else:
                length = e
                grab_char = True

    return "".join(result)


if __name__ == "__main__":
    print(rle_decode([2, 'a', 'b', 3, 'c', 'd', 4, 'e', 3, 'a']))

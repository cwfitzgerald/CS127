#!/usr/bin/env python3


def fizzbuzz(x: int) -> str:
    if (x % 15 == 0):
        return "fizzbuzz"
    elif (x % 5 == 0):
        return "buzz"
    elif (x % 3 == 0):
        return "fizz"
    else:
        return "{}".format(x)


if __name__ == "__main__":
    for x in range(1, 100 + 1):
        print(fizzbuzz(x))

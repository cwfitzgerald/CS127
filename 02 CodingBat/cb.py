#!/usr/bin/env python3

import typing


def string_times(str: str, n: int) -> str:
    out = str * n
    return out


def front_times(str: str, n: int) -> str:
    return str[0:3] * n


def string_bits(str: str) -> str:
    return str[::2]


def lone_sum(a: typing.Any, b: typing.Any, c: typing.Any) -> typing.Any:
    total = 0
    list = [a, b, c]
    for num in list:
        if list.count(num) == 1:
            total += num
    return total


def string_splosion(str: str) -> str:
    ans = ""
    for x in range(len(str)):
        ans += str[0:x + 1]
    return ans


def cigar_party(cigars: int, is_weekend: bool) -> bool:
    return cigars >= 40 and (cigars <= 60 or is_weekend)


def caught_speeding(speed: typing.Any, is_birthday: bool) -> int:
    if is_birthday:
        speed -= 5

    if speed >= 61 and speed <= 80:
        return 1
    elif speed > 80:
        return 2
    else:
        return 0

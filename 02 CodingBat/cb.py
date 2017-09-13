#!/usr/bin/env python3


def string_times(str, n):
    out = str * n
    return out


def front_times(str, n):
    return str[0:3] * n


def string_bits(str):
    return str[::2]


def lone_sum(a, b, c):
    total = 0
    list = [a, b, c]
    for num in list:
        if list.count(num) == 1:
            total += num
    return total


def string_splosion(str):
    ans = ""
    for x in range(len(str)):
        ans += str[0:x + 1]
    return ans


def cigar_party(cigars, is_weekend):
    return cigars >= 40 and (cigars <= 60 or is_weekend)


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed >= 61 and speed <= 80:
        return 1
    elif speed > 80:
        return 2
    else:
        return 0

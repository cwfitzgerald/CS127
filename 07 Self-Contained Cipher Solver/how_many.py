#!/usr/bin/env python3

import typing
import bisect


def freq(n: int, l: typing.List[int]) -> int:
    '''Find frequency of n in l'''
    s = sorted(l)  # sort array without modifying it
    index = bisect.bisect_left(s, n)  # binary search for the number

    # Count total instances
    total = 0
    for x in s[index:]:
        if x == n:
            total += 1
        else:
            # if we find a non-match, we're done, the list is sorted
            break

    return total


# Overrides builtin min
def min(l: typing.List[int]) -> int:
    '''Find minimum value in l'''
    minval = l[0]
    for x in l:
        if x < minval:
            minval = x
    return minval


def mode(l: typing.List[int]) -> int:
    '''Find mode in l'''
    s = sorted(l)
    s.append(None)  # Append None to get for loop to run once more, with the first if statement always failing

    maxval = s[0]
    maxcount = 1

    curval = s[0]
    curcount = 1

    for x in s[1:]:
        if x == curval:
            curcount += 1
        else:
            if curcount > maxcount:
                maxval = curval
                maxcount = curcount
            curval = x
            curcount = 1

    return maxval


if __name__ == "__main__":
    print(freq(3, [3, 2, 2, 1, 3, 4, 5, 4, 3, 4, 3]))
    print(min([3, 2, 2, 1, 3, 4, 5, 4, 3, 4, 3]))
    print(mode([3, 2, 2, 1, 3, 4, 5, 4, 3, 4, 3, 7, 7, 7, 7, 7, 7]))

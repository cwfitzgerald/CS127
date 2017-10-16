#!/usr/bin/env python3

# If there is a single instance of a color on the board
# you cannot make the system happy.

i = """4
7
RBY_YBR
6
X_Y__X
2
__
6
B_RRBR"""

testi = """5
1
_
4
RRGG
4
RRGR
5
RR_GR
13
RRRRRKKLSLLL_"""


def happy(gameboard):
    if len(gameboard) == 1:
        return gameboard[0] == '_'
    elif len(gameboard) == 2:
        return gameboard[0] == gameboard[1]

    if gameboard[0] != gameboard[1] and (gameboard[x] != '_'):
        return False
    for x in range(1, len(gameboard) - 1):
        if (not (gameboard[x - 1] == gameboard[x] or
                 gameboard[x + 1] == gameboard[x])) and (gameboard[x] != '_'):
            return False
    if gameboard[-2] != gameboard[-1] and (gameboard[-1] != '_'):
        return False
    return True


def solve(gameboard):
    # Count frequencies
    freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    spaces = 0

    for g in gameboard:
        if g == '_':
            spaces += 1
        else:
            freq[ord(g) - 65] += 1

    # Check if there are any with frequency 1
    return freq.count(1) == 0 and (spaces != 0 or happy(gameboard))


def main(string):
    inputs = string.split('\n')

    count = int(inputs[0])

    for x in range(count):
        length = inputs[2 * x + 1]
        gameboard = inputs[2 * x + 2]

        # print(length)
        # print(gameboard)

        solvable = solve(gameboard)

        print("YES" if solvable else "NO")

if __name__ == '__main__':
    main(i)
    # print("")
    # main(testi)

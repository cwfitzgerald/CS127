#!/usr/bin/env python3

i = """7 11
5 15
3 2
-2 2 1
5 -6"""


def main(string):
    rows = string.split('\n')
    house_left, house_right = [int(x) for x in rows[0].split()]
    apple_tree, orange_tree = [int(x) for x in rows[1].split()]
    apple_drop_length, orange_drop_length = [int(x) for x in rows[2].split()]
    apple_drops = [int(x) for x in rows[3].split()]
    orange_drops = [int(x) for x in rows[4].split()]

    apple_locations = [a + apple_tree for a in apple_drops]
    orange_locations = [o + orange_tree for o in orange_drops]

    print(sum((1 for a in apple_locations if a <= house_right and a >= house_left)))
    print(sum((1 for o in orange_locations if o <= house_right and o >= house_left)))

if __name__ == '__main__':
    main(i)

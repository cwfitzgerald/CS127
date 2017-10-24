#!/usr/bin/env python3


def divide(A, B, cake_total):
    cake_per_person = A / B
    return int(cake_total // cake_per_person)


if __name__ == "__main__":
    print(divide(5, 10, 1))        # 2
    print(divide(10, 10, 1))       # 1
    print(divide(16, 4, 60))       # 15
    print(divide(5, 10, 0))        # 0
    print(divide(1024, 512, 24))   # 12

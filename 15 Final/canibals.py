#!/usr/bin/env python3

source_data = [21, 9, 5, 8, 10, 13]


def how_many_can_i_eat(data, value):
    return sum([1 for num in data if num < value])
    # you don't have to write this but it might make things easier


def canibals(data, target):
    return sum([1 for num in data if how_many_can_i_eat(data, num) + num > target])


print("Canibals more than  5:", canibals(source_data, 5))
print("Canibals more than 10:", canibals(source_data, 10))
print("Canibals more than 15:", canibals(source_data, 15))

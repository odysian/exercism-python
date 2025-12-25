"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def is_sublist(small, large):

    if not small:
        return True

    if len(small) > len(large):
        return False

    for i in range(len(large) - len(small) + 1):

        window = large[i : i + len(small)]

        if window == small:
            return True

    return False


def sublist(list_one, list_two):

    if list_one == list_two:
        return 3

    if is_sublist(list_one, list_two):
        return 1

    if is_sublist(list_two, list_one):
        return 2

    return 4

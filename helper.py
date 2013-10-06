__author__ = 'linmichaelj'

import sys


def get_years_greater_than(arr, l_bound):
    years = 0
    for i in reversed(arr):
        if i > l_bound:
            years += 1
        else:
            break


def get_years_increasing(arr):
    prev_rev = sys.maxint
    count = 0

    for i in reversed(arr):
        curr_rev = i
        if prev_rev > curr_rev:
            prev_rev = curr_rev
            count += 1
        else:
            break
    return count

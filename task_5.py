import itertools
from functools import reduce


def multiply(seq):
    res = 1
    for _ in seq:
        res *= _
    return res


def count_find_num(primesL, limit):
    # your code here
    rep = 3
    for nums in itertools.combinations_with_replacement(primesL, rep):
        if multiply(primesL) <= multiply(nums) <= limit:
            print(nums, multiply(nums))
    print()
    rep = 4
    for nums in itertools.combinations_with_replacement(primesL, rep):
        if multiply(primesL) <= multiply(nums) <= limit:
            print(nums, multiply(nums))
    print()
    rep = 5
    for nums in itertools.combinations_with_replacement(primesL, rep):
        if (multiply(primesL) <= multiply(nums) <= limit) and (set(primesL).issubset(set(nums))):
            print(nums, multiply(nums))


count_find_num(primesL = [2, 5, 7], limit = 500)
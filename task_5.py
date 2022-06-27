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
    i = primesL[0]
    j = 0
    # while i != primesL[-1]:
    print(multiply(primesL[j+1:]) * multiply([i]*rep))

count_find_num([2, 5, 7], 500)

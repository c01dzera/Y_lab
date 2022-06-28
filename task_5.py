import itertools
from functools import reduce


def multiply(seq):
    res = 1
    for _ in seq:
        res *= _
    return res


def count_find_num(primesL, limit):
    rep = 1
    j = 0
    i = primesL[0]
    while i != primesL[-1]:
        res = multiply(primesL[j+1:]) * multiply([i]*rep)
        if res > limit:
            rep = 1
            j += 1
            i = primesL[j]
        rep += 1
        print(res)

count_find_num([2, 5, 7], 500)

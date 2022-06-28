
def multiply(seq):
    res = 1
    for _ in seq:
        res *= _
    return res


def count_find_num(primesL, limit):
    if multiply(primesL) > limit:
        return []

    res = []
    res.append(multiply(primesL))
    for i in primesL:
        for j in res:
            j *= i
            while j <= limit and j not in res:
                res.append(j)
                j *= i
    min_limit = max(res)
    cnt = len(res)
    return [cnt, min_limit]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []



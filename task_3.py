import math


def zeros(n):
	res = 0
	while n > 0:
		n /= 5
		res += math.floor(n)
	return math.floor(res)


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

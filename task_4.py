import itertools


def bananas(s):
    result = set()
    length = len('banana')
    if len(s) >= len('banana'):
        for i in itertools.combinations(s, 6):
            if 'banana' in ''.join(i):
                print(''.join(i))


bananas('bbananana')
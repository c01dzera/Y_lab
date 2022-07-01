import itertools


def bananas(s) -> set:
    result = set()

    for inx in itertools.combinations(range(len(s)), len(s)-6):
        ban = list(s)
        for i in inx:
            ban[i] = '-'
        ban = ''.join(ban)
        if ban.replace('-', '') == 'banana':
            result.add(ban)

    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

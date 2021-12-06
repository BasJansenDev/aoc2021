from functools import lru_cache


def main(inp, days):
    fishlist = [int(j) for j in [i.split(',') for i in inp][0]]
    total = 0
    for fish in fishlist:
        total += recurse(fish, days)
    return total


@lru_cache(maxsize=None)
def recurse(value, days):
    if days <= value:
        return 1
    else:
        return recurse(8, days - value - 1) + recurse(6, days - value - 1)


def input_as_list(inp):
    f = open(inp)
    return list(f.read().splitlines())


print('Part 1: ' + str(main(input_as_list('input'), 80)))
print('Part 2: ' + str(main(input_as_list('input'), 256)))

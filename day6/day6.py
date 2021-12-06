from functools import lru_cache


def main(inp, days):
    fishlist = [int(j) for j in [i.split(',') for i in inp][0]]
    return sum(recurse(fish,days) for fish in fishlist)


@lru_cache(maxsize=None)
def recurse(value, days):
    return 1 if days <= value else recurse(8, days - value - 1) + recurse(6, days - value - 1)


def input_as_list(inp):
    f = open(inp)
    return list(f.read().splitlines())


print('Part 1: ' + str(main(input_as_list('input'), 80)))
print('Part 2: ' + str(main(input_as_list('input'), 256)))

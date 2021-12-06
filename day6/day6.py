from functools import lru_cache


def main(inp, days):
    return sum(recurse(fish,days) for fish in [int(j) for j in [i for i in inp]])


@lru_cache(maxsize=None)
def recurse(value, days):
    return 1 if days <= value else recurse(8, days - value - 1) + recurse(6, days - value - 1)


def input_as_list(inp):
    f = open(inp)
    return list(f.read().split(','))


print('Part 1: ' + str(main(input_as_list('input'), 80)))
print('Part 2: ' + str(main(input_as_list('input'), 256)))

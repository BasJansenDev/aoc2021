import collections


def add_or_update(dictionary, key, times):
    if key in dictionary:
        dictionary.update({key: dictionary[key] + times})
    else:
        dictionary[key] = times


def main(inp, steps):
    polymer = inp[0]
    rules = dict(inp[1])
    char_count = dict(collections.Counter(polymer))
    pair_count = dict()
    for i in range(len(polymer) - 1):
        add_or_update(pair_count, polymer[i] + polymer[i + 1], 1)
    for step in range(steps):
        temp_count = pair_count.copy()
        for pair in pair_count:
            times = pair_count[pair]
            val = rules[pair]
            add_or_update(temp_count, pair, -times)
            add_or_update(char_count, val, times)
            add_or_update(temp_count, pair[0] + val, times)
            add_or_update(temp_count, val + pair[1], times)
        pair_count = temp_count.copy()
    return max(char_count.values()) - min(char_count.values())


def input_as_list(inp):
    f = open(inp)
    polymer, rules = f.read().split('\n\n')
    rules = [p.split(' -> ') for p in rules.splitlines()]
    return polymer, rules


print('Part 1: ' + str(main(input_as_list('input'), 10)))
print('Part 2: ' + str(main(input_as_list('input'), 40)))

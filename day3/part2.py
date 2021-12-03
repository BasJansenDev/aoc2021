def main():
    lst = inputAsList()
    a = calc(lst, False)
    b = calc(lst, True)
    return int(a, 2) * int(b, 2)

def calc(res, inv):
    idx = 0

    # For bits[idx], take the sum to determine if 0 or 1 is the most common for that bit.
    # Then, filter the original list based on whether a set of bits has the most common bit in idx.
    # The inv parameter inverses the results, taking the least common bit for an index instead.
    # Repeat until there is only one entry left.

    while len(res) > 1:
        res = list(filter(lambda bits : int(bits[idx]) == ((sum(int(bits[idx]) for bits in res) >= len(res) / 2) ^ inv),res))
        idx += 1
    return res[0]

def inputAsList():
    f = open('input')
    return list(f.read().splitlines())

print(main())

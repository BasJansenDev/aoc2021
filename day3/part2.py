def main():
    lst = inputAsList()
    a = calc(lst, False)
    b = calc(lst, True)
    return int(a, 2) * int(b, 2)

def calc(res, inv):
    idx = 0

    # For bits[idx], take the sum and check if it's greater than half the length of the input
    # to determine the most common bit for idx.
    # The `inv` parameter inverses the results, taking the least common bit for an index instead.
    # Then, filter the input based on whether a set of bits has the most/least (depending on `inv`) common bit in idx.
    # Repeat until there is only one entry left.

    while len(res) > 1:
        res = list(filter(lambda bits : int(bits[idx]) == ((sum(int(bits[idx]) for bits in res) >= len(res) / 2) ^ inv),res))
        idx += 1
    return res[0]

def inputAsList():
    f = open('input')
    return list(f.read().splitlines())

print(main())

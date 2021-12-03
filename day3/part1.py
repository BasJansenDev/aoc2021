from functools import reduce


def main():
    lst = inputAsList()
    ones = [0] * len(lst[0])
    for byte in lst:
        for bit in range(len(byte)):
            ones[bit] += int(byte[bit])
    bn = reduce(lambda a, b: (a<<1) + int(b), list(map(lambda x : x > len(lst)/2,ones)))
    return bn * (2**len(lst[0])-1-bn)

def small():
    lst = inputAsList()
    bn = reduce(lambda a, b: (a << 1) + int(b), list(map(lambda x: x > len(lst) / 2, list(map(lambda bit : sum([int(byte[bit]) for byte in lst]), range(len(lst[0])))))))
    return bn * (2 ** len(lst[0]) - 1 - bn)


def inputAsList():
    f = open('input')
    return list(f.read().splitlines())

print(main())
print(small())
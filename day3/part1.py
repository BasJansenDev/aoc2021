from functools import reduce


def main():
    lst = inputAsList()
    ones = [0] * len(lst[0])
    for byte in lst:
        for bit in range(len(byte)):
            if int(byte[bit]):
                ones[bit] += 1
    bn = reduce(lambda a, b: (a<<1) + int(b), list(map(lambda x : x > len(lst)/2,ones)))
    return bn * (2**(len(lst[0]))-bn-1)

def inputAsList():
    f = open('input')
    return list(f.read().splitlines())

print(main())
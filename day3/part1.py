from functools import reduce


def main():
    lst = inputAsList()

    # Sum each bit in the list of bits by index:
    ones = list(map(lambda bit : sum([int(bits[bit]) for bits in lst]), range(len(lst[0]))))
    # Determine the most common bit by checking if the sum of ones is greater than half the number of bits.
    # Then convert binary to decimal:
    dec = reduce(lambda a, b: (a<<1) + int(b), list(map(lambda x : x > len(lst)/2, ones)))
    # Multiply value with its inverse:
    return dec * (2**len(lst[0])-1-dec)

def inputAsList():
    f = open('input')
    return list(f.read().splitlines())

print(main())
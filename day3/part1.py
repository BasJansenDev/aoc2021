
def main():
    lst = inputAsList()
    ones = [0] * len(lst[0])
    for byte in lst:
        for bit in range(len(byte)):
            if int(byte[bit]) :
                ones[bit] += 1
    bin = list(map(lambda x : x > len(lst)/2,ones))
    binInverse = [not elem for elem in bin]
    return bitshift(bin) * bitshift(binInverse)

def bitshift(bin):
    out = 0
    for bit in bin:
        out = (out << 1) | bit
    return out

def inputAsList():
    f = open('input')
    return list(f.read().splitlines())

print(main())
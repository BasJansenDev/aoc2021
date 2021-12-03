def main():
    lst = inputAsList()
    a = calc(lst, False)
    b = calc(lst, True)
    return int(a, 2) * int(b, 2)


def calc(lst, inv):
    res = lst
    idx = 0
    while len(res) > 1:
        ones = 0
        for byte in res:
            if int(byte[idx]):
                ones += 1
        mcb = ones >= len(res) / 2
        resTmp = []
        for byte in res:
            if int(byte[idx]) == (mcb ^ inv):
                resTmp += [byte]
        res = resTmp
        idx += 1
    return res[0]


def inputAsList():
    f = open('input')
    return list(f.read().splitlines())


print(main())

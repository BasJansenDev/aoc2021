def main():
    lst = inputAsList()
    a = calc(lst, False)
    b = calc(lst, True)
    return int(a, 2) * int(b, 2)

def calc(res, inv):
    idx = 0
    while len(res) > 1:
        res = list(filter(lambda byte : int(byte[idx]) == ((sum(int(byte[idx]) for byte in res) >= len(res) / 2) ^ inv),res))
        idx += 1
    return res[0]

def inputAsList():
    f = open('input')
    return list(f.read().splitlines())

print(main())

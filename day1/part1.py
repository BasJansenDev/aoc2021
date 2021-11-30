def main():
    list = inputAsList()
    print(list)


def inputAsList():
    f = open('day1/input')
    return list(map(int, f.read().splitlines()))

main()
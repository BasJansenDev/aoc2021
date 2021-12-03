def main(inp):
    print(inp)

    return 0


def input_as_list(inp):
    f = open(inp)
    return list(f.read().splitlines())


print(main(input_as_list('testinput')))
print(main(input_as_list('input')))

import operator


def main():
    lst = inputAsList()
    res = (0,0)
    aim = 0
    for i in lst:
        direction, magnitude = i.split(' ')
        direction_tuple = DIRECTIONS[direction]
        aim += direction_tuple[1] * int(magnitude)
        res = tuple(map(operator.add,res, (direction_tuple[0] * int(magnitude), direction_tuple[0] * int(magnitude) * aim)))
    return res[0]*res[1]

DIRECTIONS = {
    'forward': (1, 0),
    'down': (0,1),
    'up': (0, -1)
}
def inputAsList():
    f = open('input')
    return list(f.read().splitlines())

print(main())
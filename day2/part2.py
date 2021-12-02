import operator


def main():
    lst = inputAsList()
    res = (0,0)
    aim = 0
    for i in range (0,len(lst)):
        entry = lst[i].split(' ')
        direction = DIRECTIONS[entry[0]]
        magnitude = int(entry[1])
        aim += direction[1] * magnitude
        res = tuple(map(operator.add,res, (direction[0] * magnitude, direction[0] * magnitude * aim)))
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
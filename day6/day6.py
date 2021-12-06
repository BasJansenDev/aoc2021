def main(inp, part2):
    fishlist = [int(j) for j in [i.split(',') for i in inp][0]]
    days = 20
    for day in range (0,days):
        fishListTmp = []
        for fish in fishlist:
            if(fish == 0):
                fish = 7
                fishListTmp.append(8)
            fish -= 1
            fishListTmp.append(fish)
        fishlist = fishListTmp
        print(fishlist)
    return len(fishlist)


def input_as_list(inp):
    f = open(inp)
    return list(f.read().splitlines())


print('Part 1: ' + str(main(input_as_list('testinput'), False)))
# print('Part 2: ' + str(main(input_as_list('testinput'), True)))

def main(inp, part2):
    formatted_lines = [[[int(value) for value in elem.strip().split(',')] for elem in line.split('->')] for line in inp]
    pipes = []
    for line in formatted_lines:
        x1 = line[0][0]
        x2 = line[1][0]
        y1 = line[0][1]
        y2 = line[1][1]
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        if (x1 == x2 or y1 == y2):
            for x in range(x1, x2 + x_step, x_step):
                for y in range(y1, y2 + y_step, y_step):
                    pipes.append(tuple([x, y]))
        elif (part2):
            range_len = x2 - x1 + 1 if x1 < x2 else x1 - x2 + 1
            for dot in range(0, range_len):
                pipes.append(tuple([x1 + (dot * x_step), y1 + (dot * y_step)]))
    seen = set()
    return len(set([x for x in pipes if x in seen or seen.add(x)]))


def input_as_list(inp):
    f = open(inp)
    return list(f.read().splitlines())


print('Part 1: ' + str(main(input_as_list('input'), False)))
print('Part 2: ' + str(main(input_as_list('input'), True)))

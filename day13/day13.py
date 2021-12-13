def main(inp, partb):
    points = inp[0]
    folds = inp[1]
    for fold in folds:
        pts = set()
        fold_axis = fold[0]
        fold_value = int(fold[1])
        for point in points:
            if fold_axis == 'y' and point[1] > fold_value:
                pts.add((point[0],2*fold_value - point[1]))
            elif fold_axis == 'x' and point[0] > fold_value:
                pts.add((2*fold_value - point[0],point[1]))
            else:
                pts.add(point)
        points = pts.copy()
        if not partb:
            return len(points)
    if(partb):
        character_printer(points)
    return len(points)

def character_printer(points):
    for y in range(0,6):
        line = ""
        for x in range(0,39):
            if((x,y) in points):
                line += '#'
            else:
                line += ' '
        print(line)


def input_as_list(inp):
    f = open(inp)
    points, folds = f.read().split('\n\n')
    points = [tuple([int(q) for q in p.split(',')]) for p in points.splitlines()]
    folds = [p.split('=') for p in folds.splitlines()]
    return points,folds


print('Part 1: ' + str(main(input_as_list('input'), False)))
print('Part 2: ' + str(main(input_as_list('input'), True)))

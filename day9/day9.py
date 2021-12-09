from functools import reduce


def main(matrix):
    lowpoints = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if all(matrix[point[0]][point[1]] > matrix[y][x] for point in get_adjacent_points(matrix, y, x)):
                lowpoints.append(int(matrix[y][x]))
    return sum([point + 1 for point in lowpoints])


def main2(matrix):
    lowpoints = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if all(matrix[point[0]][point[1]] > matrix[y][x] for point in get_adjacent_points(matrix, y, x)):
                lowpoints.append((y, x))
    basin_sizes = []
    for point in lowpoints:
        basin = {point}
        last_len = 0
        while last_len != len(basin):
            last_len = len(basin)
            basinTmp = set(basin)
            for basin_point in basinTmp:
                adjacent_points = set(get_adjacent_points(matrix, basin_point[0], basin_point[1]))
                basin.update(set(list(filter(lambda adjacent_point: int(matrix[adjacent_point[0]][adjacent_point[1]]) != 9,
                                             adjacent_points))))
        basin_sizes.append(len(basin))
    return reduce((lambda size_1, size_2: size_1 * size_2), sorted(basin_sizes, reverse=True)[:3])


def get_adjacent_points(matrix, y, x):
    adjacent = []
    if y > 0:
        adjacent.append((y - 1, x))
    if y + 1 < len(matrix):
        adjacent.append((y + 1, x))
    if x > 0:
        adjacent.append((y, x - 1))
    if x + 1 < len(matrix[y]):
        adjacent.append((y, x + 1))
    return adjacent


def matrixut_as_list(matrix):
    f = open(matrix)
    return list(f.read().splitlines())


print('Part 1: ' + str(main(matrixut_as_list('input'))))
print('Part 2: ' + str(main2(matrixut_as_list('input'))))

import math
from datetime import datetime


def main(inp):
    matrix = [[int(j) for j in i] for i in inp]
    matrix_size = (len(matrix))*(len(matrix))
    unvisited = dict()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            unvisited.update({(y,x): math.inf})
    visited = {}
    current = (0,0)
    current_distance = 0
    unvisited[current] = current_distance
    while True:
        if(len(visited) % 1000 == 0):
            print("[ " + str(datetime.now())+ " ] " + "Visited " + str(len(visited)) + " out of " + str(matrix_size))
        neighbors = get_adjacent_distances(matrix,current)
        for neighbor in neighbors:
            if neighbor not in unvisited:
                continue
            new_distance = current_distance + matrix[neighbor[0]][neighbor[1]]
            if unvisited[neighbor] is math.inf or unvisited[neighbor] > new_distance:
                unvisited[neighbor] = new_distance
        visited[current] = current_distance
        del unvisited[current]
        if not unvisited or current == (len(matrix)-1,len(matrix)-1):
            break
        unvisited_candidates = {k: unvisited[k] for k in unvisited if unvisited[k] != math.inf}
        current = min(unvisited_candidates, key=unvisited_candidates.get)
        current_distance = unvisited[current]

    return visited[(len(matrix)-1,len(matrix)-1)]


def input_as_list(inp):
    f = open(inp)
    return f.read().splitlines()


def get_adjacent_distances(matrix, position):
    y = position[0]
    x = position[1]
    neighbors = dict()
    if x > 0:
        neighbors.update({(y,x-1) : matrix[y][x-1]})
    if y > 0:
        neighbors.update({(y-1,x) : matrix[y-1][x]})
    if x < len(matrix)-1:
        neighbors.update({(y,x+1) : matrix[y][x+1]})
    if y < len(matrix)-1:
        neighbors.update({(y+1,x) : matrix[y+1][x]})
    return neighbors

def large_map(inp, multiply):
    new_map = []
    for y in range(multiply*len(inp)):
        line = ""
        for mul in range(multiply):
            for x in range(len(inp)):
                new_val = int(inp[y % len(inp)][x]) + (mul + math.floor(y / len(inp)))
                line += str(new_val) if new_val < 10 else str(new_val%9)
        new_map.append(line)
    return new_map


# print('Part 1: ' + str(main(input_as_list('input'))))
print('Part 2: ' + str(main(large_map(input_as_list('input'),5))))

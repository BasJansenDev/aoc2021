from collections import defaultdict

edges = defaultdict(list)
def main(inp,partb):
    for edge in inp:
        node1, node2 = edge.split('-')
        edges[node1].append(node2)
        edges[node2].append(node1)
    paths = recursive_path('start', [], [], None, partb)
    return len(paths)

def recursive_path(cave, path, visited, seen_twice, partb):
    path.append(cave)
    if cave == 'end':
        return [path]
    if cave.islower():
        visited.append(cave)
    paths = []
    for next_cave in edges[cave]:
        if next_cave not in visited:
            paths += recursive_path(next_cave, path[:], visited[:], seen_twice, partb)
        elif partb and seen_twice is None and next_cave != 'start':
            paths += recursive_path(next_cave, path[:], visited[:], next_cave, partb)
    return paths


def input_as_list(inp):
    f = open(inp)
    return list(f.read().splitlines())

# Can only activate one at a time
# print('Part 1: ' + str(main(input_as_list('input'), False)))
print('Part 2: ' + str(main(input_as_list('input'), True)))

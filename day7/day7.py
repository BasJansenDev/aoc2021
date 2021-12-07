import math

def oneliner(c_p, b):
    return min(list(map(lambda d: sum([((abs(d-c)*(abs(d-c)+1))/2) if b else abs(d - c) for c in c_p]), range(min(c_p), max(c_p)+1))))

# The shortest position will be between the lowest and highest position of crabs
# Calculate the sum of differences between each crab's position and a possible position
# Calculate the minimum value of these sums for each possible position
# Return the answer
def main(crab_people, partb):
    min_dist = math.inf
    for position in range(min(crab_people), max(crab_people)+1):
        crab_distance = []
        for crab in crab_people:
            if partb:
                crab_distance.append(divergent_series(abs(position-crab)))
            else:
                crab_distance.append(abs(position-crab))
        min_dist = min(sum(crab_distance),min_dist)
    return min_dist

def divergent_series(n):
    return (n*(n+1))/2

def input_as_list(inp):
    f = open(inp)
    return [int(j) for j in [i for i in list(f.read().split(','))]]

print('Part 1: ' + str(main(input_as_list('input'),False)))
print('Part 2: ' + str(main(input_as_list('input'),True)))

def main(inp, partb):
    fail = 0
    incomplete_lines = []
    for block in inp:
        failed = False
        character_stack = []
        for chr in block:
            if chr in '{([<':
                character_stack.append(chr)
            else:
                if chr == closers[character_stack[-1]]:
                    character_stack.pop()
                else:
                    fail += points[chr]
                    failed = True
                    break
        if not failed:
            incomplete_lines.append(character_stack)
    if(not partb):
        return fail
    else:
        pts_total = []
        for line in incomplete_lines:
            pts = 0
            leftover = line
            for i in range(0, len(line)):
                last = leftover.pop()
                pts = 5 * pts + points2[last]
            pts_total.append(pts)
        return sorted(pts_total)[int(len(pts_total) / 2)]

closers = {
    '{' : '}',
    '(' : ')',
    '[' : ']',
    '<' : '>'
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def input_as_list(inp):
    f = open(inp)
    return list(f.read().splitlines())


print('Part 1: ' + str(main(input_as_list('input'), False)))
print('Part 2: ' + str(main(input_as_list('input'), True)))

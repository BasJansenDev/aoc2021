def main(inp, partb, maxsteps):
    octos = inp
    flash_count = 0
    for step in range(0,maxsteps):
        octos = [(list(map(lambda octo: octo + 1, row))) for row in octos]
        flashers = []
        while True:
            flash = check_nines(octos)
            flashers += flash
            flashed = get_adjacent_octos(octos, flash)
            if (partb and len(flashers) == len(octos) * len(octos)):
                return step + 1
            if flashed == []:
                break
            else:
                add_one_to_flashed(octos, flashed, flashers)
        flash_count += len(flashers)
    return flash_count


def add_one_to_flashed(octos, flashed, flashers):
    for position in flashed:
        if position not in flashers:
            octos[position[0]][position[1]] += 1
    return octos


def check_nines(octos):
    flashers = []
    for octo_y in range(0, len(octos)):
        for octo_x in range(0, len(octos)):
            if octos[octo_x][octo_y] > 9:
                flashers.append([octo_x, octo_y])
                octos[octo_x][octo_y] = 0
    return flashers


def get_adjacent_octos(octos, flash):
    adj = []
    for f in flash:
        x = f[0]
        y = f[1]
        x_val_low = x - 1 if x != 0 else x
        x_val_top = x + 1 if x != len(octos) - 1 else x
        y_val_low = y - 1 if y != 0 else y
        y_val_top = y + 1 if y != len(octos) - 1 else y
        adj += [[row, col] for row in range(x_val_low, x_val_top + 1) for col in range(y_val_low, y_val_top + 1) if
                [row, col] != [x, y]]
    return adj


def input_as_list(inp):
    f = open(inp).read().splitlines()
    return [[int(j) for j in i] for i in f]


print('Part 1: ' + str(main(input_as_list('input'), False, 100)))
print('Part 2: ' + str(main(input_as_list('input'), True, 10000)))

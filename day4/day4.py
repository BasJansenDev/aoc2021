def main(inp,part1):
    numbers = inp[0].split(',')
    boards = make_board_matrix(inp[1:])
    for number in numbers:
        boardTmp = []
        for board in boards:
            updatedBoard = list(map(lambda row : [0 if number == value else value for value in row], board))
            if not board_check(updatedBoard):
                boardTmp.append(updatedBoard)
            else:
                if part1:
                    return int(number) * calculate_total(updatedBoard)
                elif len(boards) == 1:
                    return int(number) * calculate_total(updatedBoard)
        boards = boardTmp
    return 0

def board_check(board):
    transposedBoard = list(map(list,(zip(*board))))
    a = True in list(map(lambda row : all(value == 0 for value in row),board))
    b = True in list(map(lambda row : all(value == 0 for value in row),transposedBoard))
    return a or b


def calculate_total(board):
    return sum([sum(int(i) for i in row) for row in board])

def input_as_list(inp):
    f = open(inp)
    return list(f.read().split('\n\n'))

def make_board_matrix(inp):
    boards = []
    for board in [j.splitlines() for j in inp]:
        boards.append([i.replace('  ',' ').strip(' ').split(' ') for i in board])
    return boards

print('Part 1: ' + str(main(input_as_list('input'),True)))
print('Part 2: ' + str(main(input_as_list('input'),False)))

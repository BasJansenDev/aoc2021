def main1(inp):
    numbers = inp[0].split(',')
    boards = make_board_matrix(inp[1:])
    for number in numbers:
        boardTmp = []
        for board in boards:
            updatedBoard = list(map(lambda row : [0 if number == value else value for value in row], board))
            boardTmp.append(updatedBoard)
            if(board_check(updatedBoard)):
                return int(number) * calculate_leftover(updatedBoard)
        boards = boardTmp
    return 0

def main2(inp):
    numbers = inp[0].split(',')
    boards = make_board_matrix(inp[1:])
    for number in numbers:
        boardTmp = []
        for board in boards:
            updatedBoard = list(map(lambda row : [0 if number == value else value for value in row], board))
            win = board_check(updatedBoard)
            if not win:
                boardTmp.append(updatedBoard)
            elif len(boards) == 1:
                return int(number) * calculate_leftover(updatedBoard)
        boards = boardTmp
    return 0


def board_check(board):
    transposedBoard = list(map(list,(zip(*board))))
    a = True in list(map(lambda row : all(value == 0 for value in row),board))
    b = True in list(map(lambda row : all(value == 0 for value in row),transposedBoard))
    return a or b


def calculate_leftover(board):
    totalSum = 0
    for row in board:
        totalSum += sum(int(i) for i in row)
    return totalSum


def input_as_list(inp):
    f = open(inp)
    return list(f.read().split('\n\n'))

def make_board_matrix(inp):
    boards = []
    for board in [j.splitlines() for j in inp]:
        boards.append([i.replace('  ',' ').strip(' ').split(' ') for i in board])
    return boards

print('Part 1: ' + str(main1(input_as_list('input'))))
print('Part 2: ' + str(main2(input_as_list('input'))))

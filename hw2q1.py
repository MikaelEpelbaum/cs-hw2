from math import sqrt


def board_reader(length):
    print("Please enter a solution:")
    board = []
    for i in range(length):
        line = str(input())
        board.append([int(x) for x in line.split(' ')])
    return board


def self_sort(line, index):
    if index >= 0:
        if line[index + 1] < line[index]:
            temp = line[index + 1]
            line[index + 1] = line[index]
            line[index] = temp
    for i in range(len(line)):
        if i < len(line) - 1:
            if line[i + 1] == line[i]:
                return False
            if not line[i + 1] > line[i]:
                self_sort(line, i)
        else:
            return line


def check_rows(length, board):
    for row in range(0, length):
        line = []
        for col in range(0, length):
            line.append(board[row][col])
        line = self_sort(line, 0)
        if not line:
            return line
        for i in range(0, length):
            if line[i] != i+1:
                return False
    return True


def check_columns(length, board):
    for row in range(0, length):
        line = []
        for col in range(0, length):
            line.append(board[col][row])
        line.sort()
        for i in range(0, length):
            if line[i] != i+1:
                return False
    return True


def check_cubes(length, board):
    for i in range(0, int(sqrt(length))):
        for j in range(0, int(sqrt(length))):
            cube = []
            for row in range(i * int(sqrt(length)), (i+1) * int(sqrt(length))):
                for col in range(j * int(sqrt(length)), (j + 1) * int(sqrt(length))):
                    cube.append(board[row][col])
            cube.sort()
            for k in range(0, length):
                if cube[k] != k + 1:
                    return False
    return True


def check_board_validity(length, board):
    rows = check_rows(length, board)
    columns = check_columns(length, board)
    cubes = check_cubes(length, board)
    return columns and rows and cubes


print("Please enter the side of the board:")
length = int(input())
length_validity = int(sqrt(length)) == sqrt(length)
board = board_reader(length)
if length_validity:
    board_validity = check_board_validity(length, board)
    if board_validity:
        print('Valid Solution!')
    else:
        print('Invalid Solution')
else:
    print('Invalid Solution')
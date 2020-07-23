import pprint

def solve(board):
    """
    Solve a sudoku board
    """
    find = find_empyt(board)
    if find:
        row, col = find
    else:
        return True
    
    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

                board[row][col] = 0

def valid(board, pos, num):
    """
    Returns if move is valid
    """

    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return  False

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

board = [
    [0, 2, 0, 4, 5, 6, 7, 8, 9],
    [4, 5, 7, 0, 8, 0, 2, 3, 6],
    [6, 8, 9, 2, 3, 7, 0, 4, 0],
    [0, 0, 5, 3, 6, 2, 9, 7, 4],
    [2, 7, 4, 0, 9, 0, 6, 5, 3],
    [3, 9, 6, 5, 7, 4, 8, 0, 0],
    [0, 4, 0, 6, 1, 8, 3, 9, 7],
    [7, 6, 1, 0, 4, 0, 5, 2, 8],
    [9, 3, 8, 7, 2, 5, 0, 6, 0]
]

print(valid(board, (0,1), 1))


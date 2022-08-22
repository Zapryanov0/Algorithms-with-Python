def print_board(board):
    for row in board:
        print(*row, sep=' ')
    print()


def place_is_free(row, col, rows, cols, left_diagonals, right_diagonals):
    if row in rows or col in cols:
        return False
    if row - col in left_diagonals or row + col in right_diagonals:
        return False

    return True


def set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def queens(row, board, rows, cols, left_diagonals, right_diagonals):
    if row == 8:
        print_board(board)
        return

    for col in range(8):
        if place_is_free(row, col, rows, cols, left_diagonals, right_diagonals):
            set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)
            queens(row + 1, board, rows, cols, left_diagonals, right_diagonals)
            remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)


n = 8
board = []
[board.append(['-'] * n) for _ in range(8)]

queens(0, board, set(), set(), set(), set())

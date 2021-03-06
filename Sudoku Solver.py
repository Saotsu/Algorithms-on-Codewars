#https://www.codewars.com/kata/5296bc77afba8baa690002d7

def check(x, y, v, sudoku):
    xi = (x // 3) * 3
    yi = (y // 3) * 3

    for row in range(0, 3):
        if v in sudoku[row+yi][xi:xi+3]:
            return False

    if v in sudoku[y]:
        return False
    elif v in [row[x] for row in sudoku]:
        return False

    return True

def sudoku(puzzle):
    m, n = 0, 0
    for y in range(9):
         for x in range(9):
             if puzzle[y][x] == 0:
                 m, n = x, y
    def solve(puzzle, m, n):
        for y in range(9):
            for x in range(9):
                if puzzle[y][x] == 0:
                    for v in range(1, 10):
                        if check(x, y, v, puzzle):
                            puzzle[y][x] = v
                            solve(puzzle, m, n)
                            if puzzle[n][m] != 0:
                                return puzzle
                            puzzle[y][x] = 0
                    else:
                        return None
    return solve(puzzle, m, n)

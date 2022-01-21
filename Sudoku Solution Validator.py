#https://www.codewars.com/kata/529bf0e9bdf7657179000008

def valid_solution(board):
    for y in range(0, 7, 3):
       for x in range(0, 7, 3):
            if len(set(board[y][x:x+3]+board[y+1][x:x+3]+board[y+2][x:x+3])) != 9:
                return False
                
    for y in board:
        if len(set(y)) != 9:
            return False

    for x in range(9):
        if len(set([board[y][x] for y in range(9)])) != 9:
            return False

    return True

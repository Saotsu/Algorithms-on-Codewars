#https://www.codewars.com/kata/529bf0e9bdf7657179000008

def valid_solution(board):
    for g in range(3):
       for h in range(3):
            y = g * 3
            x = h * 3
            if len(set(board[y][x:x+3]+board[y+1][x:x+3]+board[y+2][x:x+3])) != 9:
                return False
                
    for y in board:
        if len(set(y)) != 9:
            return False

    for x in range(9):
        if len(set([board[y][x] for y in range(9)])) != 9:
            return False

    return True

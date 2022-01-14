#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    if n < 10:
        return 0
    r = 1
    for n in str(n):
        r *= int(n)
    return 1 + persistence(r)

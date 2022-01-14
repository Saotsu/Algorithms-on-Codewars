#https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd

def mygcd(x,y):
    d = max(x, y) % min(x, y)
    if d > 0: 
        return 0 + mygcd(d, min(x, y))
    return min(x, y)

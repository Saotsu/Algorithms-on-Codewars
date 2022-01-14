#https://www.codewars.com/kata/54d4c8b08776e4ad92000835

from math import log2

def isPP(n):
    for p in range(2, int(log2(n))+1):
        if round(n**(1/p))**p == n:
            return [round(n**(1/p)), p]
    return None

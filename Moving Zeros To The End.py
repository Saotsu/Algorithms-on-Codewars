#https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
    return [n for n in array if n != 0] + array.count(0)*[0]


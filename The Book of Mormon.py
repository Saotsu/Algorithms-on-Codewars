#https://www.codewars.com/kata/58373ba351e3b615de0001c3

def mormons(starting_number, reach, target, c=0):
    if starting_number >= target:
        return 0
    return 1 + mormons(starting_number + starting_number * reach, reach, target, c+1)

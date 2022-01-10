#https://www.codewars.com/kata/52fba66badcd10859f00097e

from re import findall

def disemvowel(string_):
    return ''.join(findall('[^aeiouAEIOU]', string_))

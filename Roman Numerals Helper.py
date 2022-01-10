#https://www.codewars.com/kata/51b66044bce5799a7f000003

#This code contains interative and recursive solution for this problem

#Recursive solution

class RomanNumerals:
    h = [('CM', 900), ('CD', 400), ('XC', 90), ('XL', 40), ('IX', 9), ('IV', 4), 
         ('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]

    def to_roman(val, r=None):
        if r == None:
            r = sorted(RomanNumerals.h, key=lambda x: x[1], reverse=True)
        if not r:
            return ""
        elif val < r[0][1]:
            return "" + RomanNumerals.to_roman(val, r[1:])
        
        return r[0][0] + RomanNumerals.to_roman(val-r[0][1], r)

    def from_roman(roman_num, r=None):
        if r == None:
            r = RomanNumerals.h
        if not r:
            return 0
        elif r[0][0] not in roman_num:
            return 0 + RomanNumerals.from_roman(roman_num, r[1:])

        return r[0][1] + RomanNumerals.from_roman(roman_num.replace(r[0][0], "", 1), r)
    
#Iterative solution
    
class RomanNumerals:
    h = [('CM', 900), ('CD', 400), ('XC', 90), ('XL', 40), ('IX', 9), ('IV', 4), 
         ('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]

    def to_roman(val):
        r = sorted(RomanNumerals.h, key=lambda x: x[1], reverse=True)
        s = ''
        for i in r:
            s += i[0] * (val // i[1])
            val -= (val // i[1]) * i[1]
                
        return s
    
    def from_roman(roman_num):
        r = RomanNumerals.h
        s = 0
        for i in r:
            s += i[1] * roman_num.count(i[0])
            roman_num = roman_num.replace(i[0], "")

        return s

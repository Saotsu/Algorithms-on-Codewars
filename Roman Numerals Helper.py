#https://www.codewars.com/kata/51b66044bce5799a7f000003

#This code contains interative and recursive solution for this problem
#Recursive solution

class RomanNumerals:
    r = [('M', 1000), ('CM', 900), ('D', 500), 
        ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), 
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]

    v = [('CM', 900), ('CD', 400), ('XC', 90), ('XL', 40), ('IX', 9),('IV', 4), 
         ('M', 1000), ('D', 500),('C', 100),('L', 50),('X', 10),('V', 5),('I', 1)]

    def to_roman(val, r=None):
        if r == None:
            r = RomanNumerals.r
        s = ""
        if r:
            while val >= r[0][1]:
                val -= r[0][1]
                s += r[0][0]
            return s + RomanNumerals.to_roman(val, r[1:])
        return ""

    def from_roman(roman_num, r=None):
        if r == None:
            r = RomanNumerals.v
        g = 0
        if r:
            while r[0][0] in roman_num:
                roman_num = roman_num.replace(r[0][0], "", 1)
                g += r[0][1]
            return g + RomanNumerals.from_roman(roman_num, r[1:])
        return 0
    
    #Iterative solution
    
    class RomanNumerals:
    def to_roman(val):
        r = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), 
        ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
        s = ''
        for i in r:
            while val >= i[1]:
                val -= i[1]
                s += i[0]
        return s
    
    def from_roman(roman_num):
        r = [('CM', 900), ('CD', 400), ('XC', 90), ('XL', 40), ('IX', 9), ('IV', 4), 
         ('M', 1000), ('D', 500),('C', 100),('L', 50),('X', 10),('V', 5),('I', 1)]
        s = 0
        for i in r:
            while i[0] in roman_num:
                 roman_num = roman_num.replace(i[0], '', 1)
                 s += i[1]
        return s
      
      
      

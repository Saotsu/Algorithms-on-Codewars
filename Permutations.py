#https://www.codewars.com/kata/5254ca2719453dcc0b00027d

#Itertools
import itertools

def permutations(string):
    c = []
    for a in itertools.permutations(list(string), len(string)):
        c.append("".join(a))
    return list(set(c))

  
#Recursive
def permutations(string):
    def helper(string, c=None, l=[]):
        if c == None:
            c = ""
        if len(string) == 0:
            l.append(c)
        else:
            for i in range(len(string)):
                helper(string[:i] + string[i+1:], c + string[i], l)
        return l
    return sorted(list(set(helper(string))))

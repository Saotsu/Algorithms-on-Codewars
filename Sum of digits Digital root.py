#https://www.codewars.com/kata/541c8630095125aba6000c00

#Iterative solution
def digital_root(n):
    while len(str(n)) >= 2:
        n = sum(int(b) for b in str(n))
    return n

#Recursive solution
digital_root = lambda n: n if len(str(n)) == 1 else digital_root(sum(int(b) for b in str(n)))

#Best solution
digital_root = lambda i: [0,1+(int(i)-1)%9][i>0]

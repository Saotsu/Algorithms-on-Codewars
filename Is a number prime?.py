#https://www.codewars.com/kata/5262119038c0985a5b00029f

def is_prime(num):
    if num < 2:
        return False
    
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True

#https://www.codewars.com/kata/55aa075506463dac6600010d

def list_squared(m, n):
    def squared(number):
        s = []
        for n in range(1, int(number**0.5)+1):
            if number % n == 0:
                s.extend([n**2, int(number / n)**2])
        return sum(set(s))
    
    results = []
    for x in range(m, n):
        s = squared(x)
        if (s**0.5) % 1 == 0:
            results.append([x, s])
    return results

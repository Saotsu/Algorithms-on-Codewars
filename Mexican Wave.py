#https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(people):
    result = []
    for i in range(len(people)):
        if people[i].isalpha():
            result.append(people[:i] + people[i].upper() + people[i+1:])
    return result

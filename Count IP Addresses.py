#https://www.codewars.com/kata/526989a41034285187000de4

def ips_between(start, end):
    return (sum((int(number[1]) * 256 ** index) - (int(number[0]) * 256 ** index) for index, number in enumerate(list(zip(start.split(".")[::-1], end.split(".")[::-1])))))

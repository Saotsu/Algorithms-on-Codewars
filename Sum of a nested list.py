#https://www.codewars.com/kata/5a15a4db06d5b6d33c000018

def sum_nested(lst):
    return sum(sum_nested(e) if isinstance(e, list) else e for e in lst)

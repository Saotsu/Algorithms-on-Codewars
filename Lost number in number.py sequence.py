#https://www.codewars.com/kata/595aa94353e43a8746000120

def find_deleted_number(arr, mixed_arr):
    x = [n for n in arr if n not in mixed_arr]
    return x[0] if x else 0

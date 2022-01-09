#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    o = sorted([n for n in source_array if n % 2 != 0])
    for i, n in enumerate(source_array):
        if n % 2 != 0:
            source_array[i] = o[0]
            e.pop(0)
    return source_array

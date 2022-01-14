#https://www.codewars.com/kata/52b757663a95b11b3d00062d

def to_weird_case(string):
    if isinstance(string, str):
        string = string.split()
    for w in string:
        w = "".join(w[i].upper() if i % 2 == 0 else w[i].lower() for i in range(len(w)))
        if len(string) > 1:
            return w + " " + to_weird_case(string[1:])
        return w

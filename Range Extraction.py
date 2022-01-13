#https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    c = []
    d = 0
    for i, e in enumerate(args[1:]):
        if d == 0:
            if e - 1 == args[i]:
                d = 1
                c = [args[i]] + [e]    
            elif e + 1 == args[i]:
                d = -1
                c = [args[i]] + [e]
            else:
                return f'{args[i]},' + solution(args[i+1:])
        elif e == c[-1] + d:
            c.append(e)
        elif len(c) >= 3:
            return f'{c[0]}-{c[-1]},' + solution(args[i+1:])
        else:
            return (",".join(str(l) for l in c)) + "," + solution(args[i+1:])
    return f'{c[0]}-{c[-1]}' if len(c) >= 3 else str(args[-1]) if not c else ",".join(str(l) for l in c)

#https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order,max_e):
    s = {n: 0 for n in set(order)}
    o = []
    for n in order:
        if s[n] < max_e:
            s[n] += 1
            o.append(n)
    return o

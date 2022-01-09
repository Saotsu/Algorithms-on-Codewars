#https://www.codewars.com/kata/53368a47e38700bd8300030d

def namelist(names):
    if not names:
        return ""
    elif len(names) == 1:
        return names[0]['name']
    s = ", ".join(n['name'] for n in names)
    return s.replace(f", {names[-1]['name']}", f" & {names[-1]['name']}")

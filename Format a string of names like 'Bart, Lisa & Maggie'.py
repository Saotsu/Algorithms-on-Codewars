#https://www.codewars.com/kata/53368a47e38700bd8300030d

def namelist(names):
    if not names:
        return ""
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return " & ".join(n['name'] for n in names)
    else:
        s = ", ".join(n['name'] for n in names)
        s = s.replace(f", {names[-1]['name']}", f" & {names[-1]['name']}")
        return s

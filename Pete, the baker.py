#https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):
    i = []
    for f in recipe:
        if f in available.keys():
            i.append(available[f] // recipe[f])
        else:
            return 0
    return min(i)

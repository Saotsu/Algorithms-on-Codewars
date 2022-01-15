#https://www.codewars.com/kata/52b7ed099cdc285c300001cd

#Crazy recursive way
def sum_of_intervals(intervals):
    intervals = [*set(intervals)]
    def reduc(intervals):
        for i, j in enumerate(intervals):
            for m, n in enumerate(intervals[:i] + intervals[i+1:]):
                if any([j[0] < n[0] < j[1], j[0] < n[1] < j[1]]):
                    g = [min([*j, *n]), max([*j, *n])]   
                    return [] + reduc([x for x in intervals if x not in [j, n]] + [g])
        return intervals
    
    return sum(abs(e[0]-e[1]) for e in reduc(intervals))

#Simple way
def sum_of_intervals(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)
    return len(result)

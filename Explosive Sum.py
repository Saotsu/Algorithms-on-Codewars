#https://www.codewars.com/kata/52ec24228a515e620b0005ef

def exp_sum(n):
    array = [[1] + n*[0], (n+1)*[1]]
    for x in range(n-1):
        array.append([1 for x in range(n+1)])

    for row in range(len(array)):
        if row > 1:
            for column in range(len(array)):
                if column < row:
                    array[row][column] = array[row-1][column]
                else:
                    array[row][column] = array[row-1][column]+array[row][column-row]

    return array[-1][-1]

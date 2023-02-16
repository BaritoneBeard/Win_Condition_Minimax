def vertical_possibilities(partition):
    sum = 0
    for i in range(1, len(partition)):
        for j in range(0, len(partition[0])):
            if partition[i][j] == "" and partition[i-1][j] == "":
                sum += 1
                partition[i][j], partition[i-1][j] = 'X', 'X'
    return sum

def horizontal_possibilities(partition):
    sum = 0
    for i in range(0, len(partition)):
        for j in range(1, len(partition[0])):
            if partition[i][j] == "" and partition[i][j-1] == "":
                sum -= 1
                partition[i][j], partition[i-1][j] = 'X', 'X'
    return sum

def calc_possibilities(partition):
    sum = vertical_possibilities(partition) + horizontal_possibilities(partition)
    return sum
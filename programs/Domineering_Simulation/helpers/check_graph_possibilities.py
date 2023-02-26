def vertical_possibilities(partition):
    sum = 0
    copy = [list[:] for list in partition]  # copy matrix without sharing a reference
    for i in range(1, len(copy)):
        for j in range(0, len(copy[0])):
            if copy[i][j] != 'X' and copy[i-1][j] != 'X':
                sum += 1
                copy[i][j], copy[i-1][j] = 'X', 'X'
    print(sum)
    return sum

def horizontal_possibilities(partition):
    sum = 0
    copy = [list[:] for list in partition]  # copy matrix without sharing a reference
    for i in range(0, len(copy)):
        for j in range(1, len(copy[0])):
            if copy[i][j] != 'X' and copy[i][j-1] != 'X':
                sum -= 1
                copy[i][j], copy[i-1][j] = 'X', 'X'
    print(sum)
    return sum

def calc_possibilities(partition):
    sum = vertical_possibilities(partition) + horizontal_possibilities(partition)
    return sum
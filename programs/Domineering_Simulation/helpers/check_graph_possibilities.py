from programs.Domineering_Simulation.helpers.graph_and_board_computation import copy_list

def possible_vertical_moves(board):
    possible_moves = []
    for i in range(1, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] != 'X' and board[i - 1][j] != 'X':
                possible_moves.append([str(i) + str(j), str(i - 1) + str(j)])
    return possible_moves


def possible_horizontal_moves(board):
    possible_moves = []
    for i in range(0, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 'X' and board[i][j - 1] != 'X':
                possible_moves.append([str(i)+ str(j), str(i)+str(j-1)])
    return possible_moves


def vertical_possibilities(partition):
    sum = 0
    copy = copy_list(partition)  # copy matrix without sharing a reference
    for i in range(1, len(copy)):
        for j in range(0, len(copy[0])):
            if copy[i][j] != 'X' and copy[i-1][j] != 'X':
                sum += 1
                copy[i][j], copy[i-1][j] = 'X', 'X'
    return sum

def horizontal_possibilities(partition):
    sum = 0
    copy = copy_list(partition)  # copy matrix without sharing a reference
    for i in range(0, len(copy)):
        for j in range(1, len(copy[0])):
            if copy[i][j] != 'X' and copy[i][j-1] != 'X':
                sum -= 1
                copy[i][j], copy[i-1][j] = 'X', 'X'
    return sum

def calc_possibilities(partition):
    # the possibilities vs actual moves should be different,
    # because a move cannot be placed in both (00,01) and (00,10),
    # both of those moves may be available but only one player may take the coveted 00 spot.
    sum_of_possibilities = vertical_possibilities(partition) + horizontal_possibilities(partition)
    return sum_of_possibilities
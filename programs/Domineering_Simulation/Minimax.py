from programs.Domineering_Simulation.helpers.check_partition_existence import check_partition_existence
from programs.Domineering_Simulation.helpers.check_graph_possibilities import calc_possibilities, \
                                                                              possible_horizontal_moves, \
                                                                              possible_vertical_moves



def Minimax(player, graph, board, depth):
    if depth >= 0 or (check_partition_existence(graph, 'S','N') == True and check_partition_existence(graph, 'E','W') == True):
        return calc_possibilities(board)

    if player == 1:
        value = -9999
        possible_moves = possible_vertical_moves(board)
        for move in possible_moves:
            value = max(value, Minimax(player*-1, graph, move, depth -1))
        return value
    else:
        value = 9999
        possible_moves = possible_horizontal_moves(board)
        for move in possible_moves:
            value = min(value, Minimax(player*-1, graph, move, depth-1))
        return value
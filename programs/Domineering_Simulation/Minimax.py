from programs.Domineering_Simulation.helpers.check_partition_existence import check_partition_existence
from programs.Domineering_Simulation.helpers.check_graph_possibilities import calc_possibilities, \
    possible_horizontal_moves, \
    possible_vertical_moves
from programs.Domineering_Simulation.helpers.graph_and_board_computation import copy_list, \
    add_move, \
    build_graph_from_board, \
    generate_empty_8x8_graph, \
    print_board

def Minimax(player, graph, board, depth):
    partition = False
    if check_partition_existence(graph, 'E', 'W') is True and check_partition_existence(graph, 'N', 'S') is True:
        partition = True
        print("Partitioned!")
        print_board(board)
    if depth <= 0 or partition is True:
        return calc_possibilities(board)
    if player == 1:
        value = -9999
        possible_moves = possible_vertical_moves(board)
        for move in possible_moves:
            copy = copy_list(board)
            add_move(move=move, board=copy)
            new_graph = generate_empty_8x8_graph()
            build_graph_from_board(graph=new_graph, board=copy)
            value = max(value, Minimax(player * -1, new_graph, copy, depth - 1))
        return value
    else:
        value = 9999
        possible_moves = possible_horizontal_moves(board)
        for move in possible_moves:
            copy = copy_list(board)
            add_move(move=move, board=copy)
            value = min(value, Minimax(player * -1, graph, copy, depth - 1))
        return value

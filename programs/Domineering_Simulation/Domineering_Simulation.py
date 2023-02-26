from programs.Domineering_Simulation.helpers.check_partition_existence import check_partition_existence
from programs.Domineering_Simulation.helpers.check_graph_possibilities import calc_possibilities
from programs.Domineering_Simulation.helpers.graph_and_board_computation import *

#
from programs.Domineering_Simulation.Minimax import *

def main():
    graph, board = generate_empty_graph_and_matrix(8,8)
    graph, board = fill_graph_and_board(file = 'graphs.txt', graph = graph, board = board)
    print(graph, end='\n\n')

    partition = check_partition_existence(graph, 'E', 'W')
    if partition:
        partition = check_partition_existence(graph, 'S', 'N')
        if partition:
            print("This board is partitioned into 4 quadrants")
        else:
            print("No North-South partition")
    else:
        print("No East-West partition")

    add_move(move = ['02','12'], board = board, graph = graph,)

    # print(graph, end='\n\n')
    # print(board)

    print(calc_possibilities(board))

    print(possible_vertical_moves(board))
    print(len(possible_vertical_moves(board)))
    print(possible_horizontal_moves(board))
    print(len(possible_horizontal_moves(board)))

if __name__ == '__main__':
    main()
from programs.Domineering_Simulation.helpers.check_partition_existence import check_partition_existence
from programs.Domineering_Simulation.helpers.check_graph_possibilities import calc_possibilities
from programs.Domineering_Simulation.helpers.graph_and_board_computation import *
from programs.Domineering_Simulation.Minimax import *



def main():
    file = 'graphs.txt'
    graph, board = generate_empty_graph_and_matrix(8,8)
    # graph = fill_graph(file = file, graph = graph)
    board = fill_board(file = file, board = board)
    build_graph_from_board(graph=graph, board=board)

    partition = check_partition_existence(graph, 'E', 'W')
    if partition:
        partition = check_partition_existence(graph, 'S', 'N')
        if partition:
            print("This board is partitioned into 4 quadrants")
        else:
            print("No North-South partition")
    else:
        print("No East-West partition")

    # print(graph, end='\n\n')
    # print(board)
    print(graph)
    print_board(board)

    # print(calc_possibilities(board))
    print()
    Minimax(1,graph,board,2)
    print()
    print_board(board)
    print(graph)

if __name__ == '__main__':
    main()
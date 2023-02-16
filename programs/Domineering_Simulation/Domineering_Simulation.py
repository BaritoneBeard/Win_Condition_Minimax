from programs.Domineering_Simulation.helpers.check_partition_existence import check_partition_existence
from programs.Domineering_Simulation.helpers.check_graph_possibilities import calc_possibilities
from programs.Domineering_Simulation.helpers.graph_and_board_computation import *

def main():
    graph, board = generate_empty_graph_and_matrix(8,8)
    graph = fill_graph('graphs.txt', graph)
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



if __name__ == '__main__':
    main()
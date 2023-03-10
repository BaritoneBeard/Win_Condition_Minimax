from programs.Domineering_Simulation.helpers.graph_and_board_computation import *
from programs.Domineering_Simulation.Minimax import *
import time


def main():
    file = 'graphs.txt'
    graph = generate_empty_8x8_graph()
    board = generate_empty_8x8_board()
    board = fill_board(file=file, board=board)
    build_graph_from_board(graph=graph, board=board)
    print_board(board)

    delta = time.time()
    possible_first_moves = Minimax(AI_player=-1, graph=graph, board=board, depth=5).winning_moves
    print(time.time() - delta)
    filtered_list = {k for k in possible_first_moves if possible_first_moves[k] < 0}
    print(f"\nThe full list of moves and their values: {possible_first_moves} \n"
          f"List of moves which guarantee AI the win: {filtered_list}")

if __name__ == '__main__':
    main()

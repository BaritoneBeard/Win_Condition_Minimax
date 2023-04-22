from programs.Domineering_Simulation.Minimax import *
import programs.Domineering_Simulation.trad_Minimax as tm
import time


def main():
    file = 'graphs.txt'
    height = 5
    length = 5
    graph = generate_empty_graph(height=height, length=length)
    print(graph)
    board = generate_empty_board(height, length)
    board = fill_board(file=file, board=board)
    build_graph_from_board(graph=graph, board=board)
    print_board(board)
    depth = 5
    player = 1

    if player == 1:
        print('AI player is Vertical')
    else:
        print('AI player is Horizontal')
    for depth in range(1, depth+1):
        delta = time.time()
        traditional_minimax = tm.Minimax(AI_player=player, graph=graph, board=board, depth=depth)
        # trad_wins = tm.Minimax(AI_player=-1, graph=graph, board=board, depth=depth).found_end
        traditional_minimax_time = time.time() - delta

        delta = time.time()
        wincon_minimax = Minimax(AI_player=player, graph=graph, board=board, depth=depth)
        possible_first_moves = wincon_minimax.winning_moves
        # wincon_wins = wincon_minimax.found_end
        wincon_minimax_time = time.time() - delta

        print(f"\nTime comparison at recursive depth: {depth}\n"
              f"Traditional Minimax: {traditional_minimax_time} \n"
              f"Win Condition Minimax: {wincon_minimax_time}")

        # print(f"\nNumber of solved games: \n"
        #       f"Traditional Minimax: {trad_wins}\n"
        #       f"Win Condition Minimax: {wincon_wins}")

        filtered_list = {k for k in possible_first_moves if possible_first_moves[k] < 0}
        # print(f"\nThe full list of moves and their values: {possible_first_moves} \n"
        #       f"List of moves which guarantee AI the win: {filtered_list}")
        print(f"Moves found by wincon Minimax which guarantee an AI win: {filtered_list}")

if __name__ == '__main__':
    main()

from programs.Domineering_Simulation.Minimax import *
import programs.Domineering_Simulation.trad_Minimax as tm
import time


def depth_comparison(graph, board, player = 1, stop = 99):
    depth = 1

    found_end = False
    while (found_end == False):
        game = Minimax(AI_player=player, graph=graph, board=board, depth=depth)
        game = game.winning_moves
        if game != {}:
            print('All moves found which result in a win condition board state: ', end=" ")
            if player == 1:
                print({k for k in game if game[k] > 0})
                move_to_play = max(game, key=lambda v: game[v])
                print(f"maximum value move: {move_to_play}")
            else:
                print({k for k in game if game[k] < 0})
                move_to_play = min(game, key=lambda v: game[v])
                print(f"minimum value move: {move_to_play}")

            found_end = True
        if depth >= stop:   # For larger boards we may way a stopping point to prevent long runs
            break
        depth += 1
    print(f"\nDepth Wincon Minimax stopped at: {depth} \nDepth Traditional Minimax will use: {depth}")

    second_game = tm.Minimax(AI_player=player, graph=graph, board=board, depth=depth)
    moves = second_game.winning_moves
    print(f"\nWinning moves found by traditional Minimax at same depth: {moves}")


def time_comparison(graph, board, player, depth):
    for depth in range(1, depth+1):
        delta = time.time()
        traditional_minimax = tm.Minimax(AI_player=player, graph=graph, board=board, depth=depth)
        traditional_minimax_time = time.time() - delta

        delta = time.time()
        wincon_minimax = Minimax(AI_player=player, graph=graph, board=board, depth=depth)
        wincon_minimax_time = time.time() - delta

        print(f"\nTime comparison at recursive depth: {depth}\n"
              f"Traditional Minimax: {traditional_minimax_time} \n"
              f"Win Condition Minimax: {wincon_minimax_time}")




def main(time_test = False, depth_test = False):
    file = 'graphs.txt'
    height = 5
    length = 5
    graph = generate_empty_graph(height=height, length=length)
    board = generate_empty_board(height, length)
    board = fill_board(file=file, board=board)
    build_graph_from_board(graph=graph, board=board)
    print_board(board)
    depth = 5
    player = 1

    print(graph)
    if player == 1:
        print('\nAI player is Vertical\n')
    else:
        print('\nAI player is Horizontal\n')

    if time_test == True:
        time_comparison(graph=graph, board=board, player=player, depth=depth)

    if depth_test == True:
        depth_comparison(graph=graph, board=board, player=player)

if __name__ == '__main__':
    main(time_test = False, depth_test = True)

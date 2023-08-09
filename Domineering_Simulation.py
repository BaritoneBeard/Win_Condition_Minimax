from programs.Domineering_Simulation.Minimax import *
import programs.Domineering_Simulation.trad_Minimax as tm
import time
import random

def generate_graphs_txt(num_moves, board_dimensions):
    player = random.choice([0, 1])
    already_done = []
    for i in range(num_moves):

        first_buffer = random.randint(2,(board_dimensions[player]-2))
        direction = random.choice([-1, 1])

        # vertical
        if player == 1:
            first_number = str(first_buffer) + str(first_buffer + random.choice([-1,0,1]))
            second_buffer = int(first_number) + (direction * 10)
            second_number = str(second_buffer)
        else:
            first_number = str(first_buffer) + str(first_buffer + random.choice([-1,0,1]))
            second_buffer = int(first_number) + direction
            second_number = str(second_buffer)
            if int(second_number[-1]) == board_dimensions[player]:
                second_number = str(int(second_number) - 2)
        print(first_number, end=' ')
        print(second_number)

        if int(first_number) < 10:
            first_number = '0' + first_number

        if int(second_number) < 10:
            second_number = '0' + second_number

        if first_number or second_number not in already_done:
            already_done.append(first_number)
            already_done.append(second_number)

        player = (player + 1) % 2

    print(already_done)
    f = open("graphs.txt", "w")
    for i in range(0, len(already_done), 2):
        f.write(already_done[i])
        f.write(' ')
        f.write(already_done[i+1])
        f.write('\n')
    f.close()




def depth_comparison(graph, board, player = 1, stop = 99):
    depth = 1
    found_end = False

    while (found_end == False):
        game = Minimax(AI_player=player, graph=graph, board=board, depth=depth)
        game = game.winning_moves
        if game != {}:
            print('All moves found which result in a win condition board state: ', end="\n")
            if player == 1:
                print({k for k in game if game[k] > 0})
                move_to_play = max(game, key=lambda v: game[v])
                print(f"\nmaximum value move: {move_to_play}")
            else:
                print({k for k in game if game[k] < 0})
                move_to_play = min(game, key=lambda v: game[v])
                print(f"\nminimum value move: {move_to_play}")

            found_end = True
        if depth >= stop:   # For larger boards we may way a stopping point to prevent long runs
            break
        depth += 1
    print(f"\nDepth Wincon Minimax stopped at: {depth} \nDepth Traditional Minimax will use: {depth}")

    second_game = tm.Minimax(AI_player=player, graph=graph, board=board, depth=depth)
    moves = second_game.winning_moves
    print(f"\nWinning moves found by traditional Minimax at same depth: {moves}")
    return depth

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


def accuracy_comparison(player, graph, board, depth):
    boards_for_accuracy = Minimax(AI_player=player, graph=graph, board=board, depth=depth, accuracy=True).winning_boards
    running_total = 0
    count_of_wins = 0
    wins = 0
    for board in boards_for_accuracy:
        winners = tm.Minimax(AI_player=player, graph=graph, board=board, depth=99).winning_players
        debug = 0
        debug_wins = 0
        if player in winners:
            wins += 1
        for win in winners:
            running_total += 1
            debug += 1
            if win == player:
                count_of_wins += 1
                debug_wins += 1
    # Uncomment these for some more User-infromation
    #         print()
    #         print_board(board)
    #         print(f"percent for this board: {(debug_wins/debug)*100}%")
    #         print(winners)
    if running_total == 0:
        return -99, -99
    accuracy = count_of_wins / running_total
    precision = wins / len(boards_for_accuracy)
    print(f"Games in which Wincon Minimax declares certain victory: {len(boards_for_accuracy)}"
          f"\n% of Games in which Traditional Minimax agrees with Wincon Minimax that there is a win: {wins / len(boards_for_accuracy) * 100}%"
          f"\n% Overall accuracy of Wincon Minimax of all possible outcomes: {accuracy * 100}%")
    return accuracy, precision


def main(player = 1, time_test = False, depth_test = False, accuracy_test = False):
    generate_graphs_txt(random.randint(5,9), [5,5])
    file = 'graphs.txt'
    height = 5
    length = 5
    graph = generate_empty_graph(height=height, length=length)
    board = generate_empty_board(height, length)
    board = fill_board(file=file, board=board)
    build_graph_from_board(graph=graph, board=board)
    print_board(board)
    depth = 5

    print(graph)
    if player == 1:
        print('\nAI player is Vertical\n')
    else:
        print('\nAI player is Horizontal\n')

    if time_test == True:
        print('\n----- Time Comparison -----\n')
        time_comparison(graph=graph, board=board, player=player, depth=depth)

    if depth_test == True:
        print('\n----- Depth Comparison -----\n')
        depth_comparison(graph=graph, board=board, player=player)

    if accuracy_test == True:
        print('\n----- Accuracy Comparison -----\n')
        accuracy_comparison(graph=graph, board=board, player=player, depth=depth)

if __name__ == '__main__':
    main(player = 1, time_test = False, depth_test = False, accuracy_test = True)

from programs.Domineering_Simulation.helpers.check_partition_existence import check_partition_existence
from programs.Domineering_Simulation.helpers.check_graph_possibilities import *
from programs.Domineering_Simulation.helpers.graph_and_board_computation import *


class Minimax:
    def __init__(self, AI_player, graph, board, depth):
        self.winning_moves = {}
        self.testing = []
        self.player = AI_player
        self.graph = graph
        self.board = board
        self.depth = depth
        self.first_move = ''
        self.alpha = -9999
        self.beta = 9999
        self.found_end = 0

        self.minimax(self.player, self.graph, self.board, self.depth, self.alpha, self.beta)


    def minimax(self, player, graph, board, depth, alpha, beta):

        # The first Base Case: Stop if the board is partitioned
        if check_partition_existence(graph, 'E', 'W') is True and check_partition_existence(graph, 'N', 'S') is True:
            # print("Partitioned!")
            # print_board(board)
            self.found_end += 1
            calculation = calc_possibilities(board)
            self.winning_moves[str(self.first_move)] = calculation
            return calculation

        # Worst case base case: If no partitions are found, might as well return something
        if depth <= 0:
            return calc_possibilities(board)

        # If depth > 0 and no partitions are found, propose a series of moves
        if player == 1:
            value = -9999
            possible_moves = possible_vertical_moves(board)
            for move in possible_moves:
                if depth == self.depth:
                    self.first_move = move
                copy, new_graph = create_copies(board=board, move=move)
                value = max(value, self.minimax(player = player * -1, graph = new_graph, board = copy, depth = depth - 1, alpha = alpha, beta = beta))
                alpha = max(value, alpha)
                if beta <= alpha:
                    break
            return value
        else:
            value = 9999
            possible_moves = possible_horizontal_moves(board)
            for move in possible_moves:
                if depth == self.depth:
                    self.first_move = move
                copy, new_graph = create_copies(board=board, move=move)
                value = min(value, self.minimax(player = player * -1, graph = new_graph, board = copy, depth = depth - 1, alpha = alpha, beta = beta))
                beta = min(value, beta)
                if beta <= alpha:
                    break
            return value


def create_copies(board, move):
    copy = copy_list(board)
    add_move(move=move, board=copy)
    new_graph = generate_empty_graph(len(board), len(board[0]))
    build_graph_from_board(graph=new_graph, board=copy)
    return copy, new_graph

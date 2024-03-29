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
        self.winning_players = []
        self.winning_boards = {}

        self.traditional_minimax(self.player, self.graph, self.board, self.depth, self.alpha, self.beta)

    def traditional_minimax(self, player, graph, board, depth, alpha, beta):
        # Worst case base case: might as well return something.
        if depth <= 0:
            return 0

        if player == 1:
            value = -9999
            possible_moves = possible_vertical_moves(board)
            if len(possible_moves) == 0:
                self.found_end += 1
                self.winning_players.append(player * -1)  # the current player has no more moves, so they lose
                return alpha
            for move in possible_moves:
                if depth == self.depth:
                    self.first_move = move
                copy, new_graph = create_copies(board=board, move=move)
                value = max(value, self.traditional_minimax(player = player * -1, graph = new_graph, board = copy, depth = depth - 1, alpha = alpha, beta = beta))
                alpha = max(value, alpha)
                if beta <= alpha:
                    break
            return value
        else:
            value = 9999
            possible_moves = possible_horizontal_moves(board)
            if len(possible_moves) == 0:
                self.found_end += 1
                self.winning_players.append(player * -1)
                return beta
            for move in possible_moves:
                if depth == self.depth:
                    self.first_move = move
                copy, new_graph = create_copies(board=board, move=move)
                value = min(value, self.traditional_minimax(player = player * -1, graph = new_graph, board = copy, depth = depth - 1, alpha = alpha, beta = beta))
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

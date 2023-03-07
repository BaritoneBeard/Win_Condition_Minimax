from programs.Domineering_Simulation.helpers.check_partition_existence import check_partition_existence
from programs.Domineering_Simulation.helpers.check_graph_possibilities import calc_possibilities, \
    possible_horizontal_moves, \
    possible_vertical_moves
from programs.Domineering_Simulation.helpers.graph_and_board_computation import copy_list, \
    add_move, \
    build_graph_from_board, \
    generate_empty_8x8_graph, \
    print_board

class Minimax:
    def __init__(self, AI_player, graph, board, depth):
        self.winning_moves = {}
        self.testing = []
        self.player = AI_player
        self.graph = graph
        self.board = board
        self.depth = depth
        self.first_move = ''
        self.minimax(self.player, self.graph, self.board, self.depth)

    def minimax(self, player, graph, board, depth):

        # The first Base Case: Stop if the board is partitioned
        if check_partition_existence(graph, 'E', 'W') is True and check_partition_existence(graph, 'N', 'S') is True:
            print("Partitioned!")
            print_board(board)
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
                value = max(value, self.minimax(player = player * -1, graph = new_graph, board = copy, depth = depth - 1))
            return value
        else:
            value = 9999
            possible_moves = possible_horizontal_moves(board)
            for move in possible_moves:
                if depth == self.depth:
                    self.first_move = move
                copy, new_graph = create_copies(board=board, move=move)
                value = min(value, self.minimax(player = player * -1, graph = new_graph, board = copy, depth = depth - 1))
            return value


def create_copies(board, move):
    copy = copy_list(board)
    add_move(move=move, board=copy)
    new_graph = generate_empty_8x8_graph()
    build_graph_from_board(graph=new_graph, board=copy)
    return copy, new_graph

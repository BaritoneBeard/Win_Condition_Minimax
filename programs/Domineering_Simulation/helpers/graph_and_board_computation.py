def copy_list(list):
    return [copy[:] for copy in list]


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            has_x = '[ ]'
            if board[i][j] == 'X':
                has_x = '[X]'
            print(has_x, end=' ')
        print()


def fill_board(file, board):
    with open(file, 'r') as document:
        for line in document:
            line = line.split()
            if not line:
                break
            for move in line:
                x, y = int(move[:1]), int(move[1:])
                if board[x][y] != 'X':
                    board[x][y] = 'X'
    return board


# :param: move should be a tuple of two digit numbers (the first digit may be 0)
def add_move(move, board, show=False):
    board[int(move[0][:1])][int(move[0][1:])] = 'X'
    board[int(move[1][:1])][int(move[1][1:])] = 'X'
    if show:
        print(f"move made: {move}")
        print_board(board)


def add_node(graph, node1, node2):
    graph[node1].append(node2)
    graph[node2].append(node1)


def build_graph_from_board(graph, board):
    for i in range(1, len(board) - 1):
        for j in range(1, len(board[i]) - 1):
            if board[i][j] == 'X':
                node1 = str(i) + str(j)
                if board[i - 1][j - 1] == 'X':
                    node2 = str(i - 1) + str(j - 1)
                    add_node(graph, node1, node2)
                if board[i - 1][j] == 'X':
                    node2 = str(i - 1) + str(j)
                    add_node(graph, node1, node2)
                if board[i - 1][j + 1] == 'X':
                    node2 = str(i - 1) + str(j + 1)
                    add_node(graph, node1, node2)
                if board[i][j - 1] == 'X':
                    node2 = str(i) + str(j - 1)
                    add_node(graph, node1, node2)
                if board[i][j] == 'X':
                    node2 = str(i) + str(j)
                    add_node(graph, node1, node2)
                if board[i][j + 1] == 'X':
                    node2 = str(i) + str(j + 1)
                    add_node(graph, node1, node2)
                if board[i + 1][j - 1] == 'X':
                    node2 = str(i + 1) + str(j - 1)
                    add_node(graph, node1, node2)
                if board[i + 1][j] == 'X':
                    node2 = str(i + 1) + str(j)
                    add_node(graph, node1, node2)
                if board[i + 1][j + 1] == 'X':
                    node2 = str(i + 1) + str(j + 1)
                    add_node(graph, node1, node2)
    return graph


def generate_empty_board(rows=8, cols=8):
    board = [[[] for x in range(cols)] for y in range(rows)]  # generate empty list for each key:value pair
    return board


def generate_empty_graph(height=8, length=8):
    graph = {}

    str_height = str(height - 1)
    str_length = str(length - 1)

    graph['W'] = []
    graph['S'] = []
    graph['N'] = []
    graph['E'] = []

    for i in range(height):
        str_i = str(i)
        graph['W'].append(str_i + '0')  # '00', '10', '20' ...
        graph[str_i + '0'] = ['W']
        graph['E'].append(str_i + str_length)  # '07', '17', '27' ...
        graph[str_i + str_length] = ['E']
    for j in range(length):
        str_j = str(j)
        graph['N'].append('0' + str_j)  # '00', '01', '02' ...
        graph['0' + str_j] = ['N']
        graph['S'].append(str_height + str_j)  # '70', '71', '72' ...
        graph[str_height + str_j] = ['S']

    for i in range(1, height - 1):  # 1:-1?
        for j in range(1, length - 1):
            graph[str(i) + str(j)] = []

    graph['00'] = ['W', 'N']
    graph['0' + str_length] = ['N', 'E']
    graph[str_height + str_length] = ['E', 'S']
    graph[str_height + '0'] = ['S', 'W']
    return graph


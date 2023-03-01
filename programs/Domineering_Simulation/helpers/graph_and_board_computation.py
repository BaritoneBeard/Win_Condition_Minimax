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


def fill_graph(file, graph):
    with open(file, 'r') as document:
        for line in document:
            line = line.split()
            if not line:
                break
            # graph
            for i in range(1,len(line)):
                graph[line[0]].append(line[i])
    return graph

def fill_board(file, board):
    with open(file, 'r') as document:
        for line in document:
            line = line.split()
            if not line:
                break
            for move in line:
                if move.isnumeric() and line[0].isnumeric():
                    x,y = int(move[:1]), int(move[1:])
                    if board[x][y] != 'X':
                        board[x][y] = 'X'
    return board

# :param: move should be a tuple of two digit numbers (the first digit may be 0)
def add_move(move, board, show=False):
    board[int(move[0][:1])][int(move[0][1:])] = 'X'
    board[int(move[1][:1])][int(move[1][1:])] = 'X'
    if show == True:
        print(f"move made: {move}")
        print_board(board)


def add_node(graph, node1, node2):
    graph[node1].append(node2)
    graph[node2].append(node1)


def build_graph_from_board(graph, board):
    if board[0][0] == 'X':
        if board[0][1] == 'X':
            add_node(graph, '00', '01')
        if board[1][0] == 'X':
            add_node(graph, '00', '10')

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 'X':
                node1 = str(i) + str(j)
                if board[i][j-1] == 'X':
                    node2= str(i) + str(j-1)
                    add_node(graph, node1, node2)
                if board[i-1][j] == 'X':
                    node2 = str(i-1) + str(j)
                    add_node(graph, node1, node2)
                if board[i-1][j-1] == 'X':
                    node2 = str(i-1) + str(j-1)
                    add_node(graph, node1, node2)
    return graph


def generate_empty_8x8_board(rows = 8, cols = 8):
    board = [[[] for x in range(cols)] for y in range(rows)]  # generate empty list for each key:value pair
    return board

#  This can be made dynamic, but it's not a top priority
def generate_empty_8x8_graph():
    graph = {}

    for i in range(8):
        for j in range(8):
            graph[str(i) + str(j)] = []

    graph['W'] = ['00', '10', '20', '30', '40', '50', '60', '70']
    graph['E'] = ['07', '17', '27', '37', '47', '57', '67', '77']
    graph['N'] = ['00', '01', '02', '03', '04', '05', '06', '07']
    graph['S'] = ['70', '71', '72', '73', '74', '75', '76', '77']
    graph['00'] = ['W', 'N']
    graph['01'] = ['N']
    graph['02'] = ['N']
    graph['03'] = ['N']
    graph['04'] = ['N']
    graph['05'] = ['N']
    graph['06'] = ['N']
    graph['07'] = ['N', 'E']
    graph['17'] = ['E']
    graph['27'] = ['E']
    graph['37'] = ['E']
    graph['47'] = ['E']
    graph['57'] = ['E']
    graph['67'] = ['E']
    graph['77'] = ['E', 'S']
    graph['76'] = ['S']
    graph['75'] = ['S']
    graph['74'] = ['S']
    graph['73'] = ['S']
    graph['72'] = ['S']
    graph['71'] = ['S']
    graph['70'] = ['S', 'W']
    graph['60'] = ['W']
    graph['50'] = ['W']
    graph['40'] = ['W']
    graph['30'] = ['W']
    graph['20'] = ['W']
    graph['10'] = ['W']
    return graph
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
def add_move(move, board):
    board[int(move[0][:1])][int(move[0][1:])] = 'X'
    board[int(move[1][:1])][int(move[1][1:])] = 'X'
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


def generate_empty_graph_and_matrix(n: int, m: int):
    rows = n
    cols = m
    dict = {}
    mat = [[[] for x in range(cols)] for y in range(rows)]  # generate empty list for each key:value pair

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            dict[str(i) + str(j)] = mat[i][j]

    dict['W'] = ['00','10','20','30','40','50','60','70']
    dict['E'] = ['07','17','27','37','47','57','67','77']
    dict['N'] = ['00','01','02','03','04','05','06','07']
    dict['S'] = ['70','71','72','73','74','75','76','77']
    dict['00'] = ['W','N']
    dict['01'] = ['N']
    dict['02'] = ['N']
    dict['03'] = ['N']
    dict['04'] = ['N']
    dict['05'] = ['N']
    dict['06'] = ['N']
    dict['07'] = ['N', 'E']
    dict['17'] = ['E']
    dict['27'] = ['E']
    dict['37'] = ['E']
    dict['47'] = ['E']
    dict['57'] = ['E']
    dict['67'] = ['E']
    dict['77'] = ['E', 'S']
    dict['76'] = ['S']
    dict['75'] = ['S']
    dict['74'] = ['S']
    dict['73'] = ['S']
    dict['72'] = ['S']
    dict['71'] = ['S']
    dict['70'] = ['S', 'W']
    dict['60'] = ['W']
    dict['50'] = ['W']
    dict['40'] = ['W']
    dict['30'] = ['W']
    dict['20'] = ['W']
    dict['10'] = ['W']
    # print(dict)
    return dict, mat
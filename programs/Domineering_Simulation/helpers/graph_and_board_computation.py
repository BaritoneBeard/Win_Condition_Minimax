def generate_empty_graph_and_matrix(n: int, m: int):
    rows = n
    cols = m
    dict = {}
    mat = [[[] for x in range(cols)] for y in range(rows)]  # generate empty list for each key:value pair

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            dict[str(i) + str(j)] = mat[i][j]
    # print(dict)
    return dict, mat


def fill_graph_and_board(file, graph, board):
    with open(file, 'r') as document:
        for line in document:
            line = line.split()
            if not line:
                continue
            # graph
            graph[line[0]] = line[1:]
            # board
            for move in line:
                if move.isnumeric() and line[0].isnumeric():
                    x,y = int(move[:1]), int(move[1:])
                    if board[x][y] != 'X':
                        board[x][y] = 'X'
    return graph


# :param: move should be a tuple of two digit numbers (the first digit may be 0)
def add_move(graph, board, move):
    graph[move[0]].append(move[1])
    graph[move[1]].append(move[0])

    board[int(move[0][:1])][int(move[0][1:])] = 'X'
    board[int(move[1][:1])][int(move[1][1:])] = 'X'
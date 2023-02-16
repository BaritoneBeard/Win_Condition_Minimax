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


def fill_graph(file, graph):
    with open(file, 'r') as document:
        for line in document:
            line = line.split()
            if not line:
                continue
            graph[line[0]] = line[1:]
    return graph

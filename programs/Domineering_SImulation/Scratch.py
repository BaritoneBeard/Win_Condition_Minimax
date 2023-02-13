# Unfinished BFS

def bfs(graph, source, end):
    visited = set()
    # bfs_traversal = list()
    queue = list()

    queue.append(source)
    visited.add(source)

    end_reached = False

    while queue:
        current_node = queue.pop(0)
        # bfs_traversal.append(current_node)
        if current_node == end:
            end_reached = True
            break

        for neighbour_node in graph[current_node]:
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append(neighbour_node)

    # print(f"BFS: {bfs_traversal}")
    return end_reached


# Generate a matrix for testing use

def generate_graph(n: int, m: int):
    rows = n
    cols = m

    dict = {}
    mat = [[[] for x in range(cols)] for y in range(rows)]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            dict[str(i) + str(j)] = mat[i][j]

    # print(dict)
    return dict


def main():
    graph = generate_graph(8,8)
    with open('graphs.txt', 'r') as document:
        for line in document:
            line = line.split()
            # if not line:
            #     continue
            graph[line[0]] = line[1:]

    print(graph)
    partition = bfs(graph, '-1-1', '05')
    print(f"partition: {partition}")


if __name__ == '__main__':
    main()
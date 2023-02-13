from programs.Domineering_Simulation.helpers.check_partition_existence import check_partition_existence

# Generate a matrix for testing use

def generate_graph(n: int, m: int):
    rows = n
    cols = m

    dict = {}
    mat = [[[] for x in range(cols)] for y in range(rows)]  # generate empty list for each key:value pair

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
            if not line:
                continue
            graph[line[0]] = line[1:]

    print(graph, end='\n\n')

    partition = check_partition_existence(graph, 'E', 'W')
    if partition:
        partition = check_partition_existence(graph, 'S', 'N')
        if partition:
            print("This board is partitioned into 4 quadrants")
        else:
            print("No North-South partition")
    else:
        print("No East-West partition")



if __name__ == '__main__':
    main()
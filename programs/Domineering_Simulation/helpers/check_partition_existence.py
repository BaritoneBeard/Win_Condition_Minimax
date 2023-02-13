def check_partition_existence(graph, source, end):
    visited = set()
    # traversal = list()
    queue = list()

    queue.append(source)
    visited.add(source)

    end_reached = False

    while queue:
        current_node = queue.pop(0)
        # traversal.append(current_node)
        if current_node == end:
            end_reached = True
            break

        for neighbour_node in graph[current_node]:
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append(neighbour_node)

    # print(f"partition path: {traversal}")
    return end_reached
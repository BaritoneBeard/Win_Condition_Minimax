def check_partition_existence(graph, source, end):
    visited = set()
    queue = list()

    queue.append(source)
    visited.add(source)

    end_reached = False

    while queue:
        current_node = queue.pop(0)
        # Breaks if we've reached our target node
        if current_node == end:
            end_reached = True
            break

        for neighbour_node in graph[current_node]:
            if neighbour_node != end:
                if neighbour_node == 'N' or neighbour_node == 'W' or neighbour_node == 'E' or neighbour_node == 'S':
                    continue  # avoid travelling using the ghost nodes
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append(neighbour_node)

    return end_reached

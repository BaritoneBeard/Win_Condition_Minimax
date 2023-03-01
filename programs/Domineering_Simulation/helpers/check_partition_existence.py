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
        # Breaks if we've reached our target node
        if current_node == end:
            # print(f"reached end: {current_node}")
            end_reached = True
            break


        for neighbour_node in graph[current_node]:
            if neighbour_node != end:
                if neighbour_node == 'N' or neighbour_node == 'W' or neighbour_node == 'E' or neighbour_node == 'S':
                    continue  # avoid travelling by way of ghost node
            if neighbour_node not in visited:
                visited.add(neighbour_node)
                queue.append(neighbour_node)

    # print(f"partition path: {traversal}")
    return end_reached
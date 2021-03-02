def bfs(graph, src):
    queue = [src]
    visited = []
    # if src not in graph:
    #     return
    visited.append(src)
    while len(queue) > 0:
        top_value = queue.pop(0)
        print(top_value)
        edges = graph.adjacent_nodes(top_value)
        for edge in edges:
            if edge in visited:
                continue
            queue.append(edge)
            visited.append(edge)
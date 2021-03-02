def depth(graph, start, k):
    def bfs(graph, src, k):
        paths = [[src]]
        visited = set()
        nodes_at_k = set()
        while len(paths) > 0:
            path = paths.pop(0)
            last_node = path[-1]
            if last_node in visited:
                continue
            if len(path) - 1 == k:
                nodes_at_k.add(last_node)
                continue
            visited.add(last_node)
            for adj in graph.adjacent_nodes(last_node):
                paths.append(path + [adj])
        return nodes_at_k
    if k == 0:
        return []
    return bfs(graph, start, k)

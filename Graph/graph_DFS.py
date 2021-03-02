def dfs(graph, src):
    stack = [src]
    visited = []
    if src not in graph:
        return
    visited.append(src)
    while len(stack) > 0:
        top_value = stack.pop()
        edges = graph.adjacent_nodes(top_value)
        for edge in edges:
            if edge in visited:
                continue
            stack.append(edge)
            visited.append(edge)
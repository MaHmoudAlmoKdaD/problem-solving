
class GraphMaze:
    directions = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]
    def __init__(self, maze):
        self.maze = maze
    def adjacent_nodes(self, node):
        y, x = node
        traversable = []
        for offset_y, offset_x in self.directions:
            current_y, current_x = y + offset_y, x + offset_x
            if not (0 <= current_y < len(self.maze)):
                continue
            if not (0 <= current_x < len(self.maze[current_y])):
                continue
            if self.maze[current_y][current_x] == "#":
                continue
            traversable.append((current_y, current_x))
        return traversable
def bfs(graph, src, dest):
    paths = [[src]]
    visited = set()
    while len(paths) > 0:
        path = paths.pop(0)
        last_node = path[-1]
        if last_node == dest:
            return path
        if last_node in visited:
            continue
        visited.add(last_node)
        for adj in graph.adjacent_nodes(last_node):
            paths.append(path + [adj])
maze = [
    "#   ",
    "##  ",
    "    "
]
print((bfs(GraphMaze(maze), (len(maze) - 1, 0), (0, len(maze[0]) - 1))))
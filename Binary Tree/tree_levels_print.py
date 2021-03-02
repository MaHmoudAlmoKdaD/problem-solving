def tree_levels(tree_node):
    if tree_node is None:
        return []
    def tree_levels_print(tree_node, fill_list):
        queue = [tree_node]
        while len(queue) > 0:
            last_node = queue.pop(0)
            if last_node is None:
                continue
            fill_list[0] = last_node.data
            queue.append(last_node.left)
            queue.append(last_node.right)
    fill_list = []
    tree_levels_print(tree_node, fill_list)
    return fill_list
def filter_bst(tree_node, a, b):
    def filter(tree_node, a, b, fill_list):
        if tree_node is None:
            return
        if tree_node.data >= a:
            filter(tree_node.left, a, b, fill_list)
        if tree_node.data < b:
            filter(tree_node.right, a, b, fill_list)
        if a <= tree_node.data < b:
            fill_list.append(tree_node.data)
    fill_list = []
    filter(tree_node, a, b, fill_list)
    return fill_list


def reverse_inplace(tree_node):
    if tree_node is None:
        return
    reverse_inplace(tree_node.left)
    reverse_inplace(tree_node.right)
    tree_node.left, tree_node.right = tree_node.right, tree_node.left
    return tree_node
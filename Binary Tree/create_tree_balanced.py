class TreeNode(object):
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def insert(self, value):
        """insert a node in a BST"""
        if self.data is None:
            self.data = value
            return

        if value < self.data:
            if self.left is None:
                self.left = TreeNode(value, self)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = TreeNode(value, self)
            else:
                self.right.insert(value)


def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid_val = len(nums) // 2
    node = TreeNode()
    node.data = nums[mid_val]
    node.left = sorted_array_to_bst(nums[:mid_val])
    node.right = sorted_array_to_bst(nums[mid_val + 1:])
    return node


def preOrder(node):
    if not node:
        return
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

def tree_levels(tree_node):
    if tree_node is None:
        return []
    def tree_levels_print(tree_node, fill_list):
        queue = [tree_node]
        while len(queue) > 0:
            last_node = queue.pop(0)
            if last_node is None:
                continue

            queue.append(last_node.left)
            queue.append(last_node.right)
        fill_list.append(tree_node.data)
        tree
        tree_levels_print(tree_node, fill_list)
    fill_list = [tree_node.data]
    tree = tree_node
    tree_levels(tree, fill_list)
    return fill_list

l = [0, 1, 2, 3, 4, 5, 6]
# tree = TreeNode()
tree = sorted_array_to_bst(l)
preOrder(tree)
print()
print(tree_levels(tree))





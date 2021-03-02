class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_list(self):
        node = self.head
        while node is not None:
            print(node, end=' ')
            node = node.next
        print('')

    def add_at_head(self, node):
        node.next = self.head
        self.head = node
        self.length += 1

    def remove_node_after(self, node):
        if node.next is not None:
            temp = node.next
            node.next = node.next.next
            temp.next = None
            self.length -= 1

    def remove_first_node(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

    def print_backward(self):
        def print_nodes_backward(node):
            if node.next is not None:
                print_nodes_backward(node.next)
            if node is not None:
                print(node, end=' ')

        if self.head is not None:
            print_nodes_backward(self.head)

        print('')

    def create_list(self, list_values):
        if len(list_values) <= 0:
            return
        next_node = Node()
        self.head = Node(list_values[0], next_node)
        l = self.head
        for i in range(1, len(list_values)):
            l.next = Node(list_values[i])
            l = l.next
            next_node = l
            self.length += 1


def merge_linked_lists(linked_list_1, linked_list_2):
    linked_list_3 = LinkedList()
    if linked_list_1.head is None:
        linked_list_3.head = linked_list_2.head
        return linked_list_3
    if linked_list_2.head is None:
        linked_list_3.head = linked_list_1.head
        return linked_list_3
    if linked_list_1.head.data < linked_list_2.head.data:
        linked_list_3.head = linked_list_1.head
        linked_list_1.remove_first_node()
    else:
        linked_list_3.head = linked_list_2.head
        linked_list_2.remove_first_node()
    current = linked_list_3.head
    while linked_list_1.head is not None and linked_list_2.head is not None:
        if linked_list_1.head.data < linked_list_2.head.data:
            current.next = linked_list_1.head
            linked_list_1.remove_first_node()
        else:
            current.next = linked_list_2.head
            linked_list_2.remove_first_node()
        current = current.next
    if linked_list_1.head is not None:
        current.next = linked_list_1.head
        return linked_list_3
    if linked_list_2.head is not None:
        current.next = linked_list_2.head
        return linked_list_3
linked_1 = LinkedList()
linked_2 = LinkedList()
l1 = [2, 4, 6, 8, 10, 13, 14, 16, 17]
l2 = []
linked_1.create_list(l1)
linked_2.create_list(l2)
# linked_1.print_list()
# linked_2.print_list()

merge_linked_lists(linked_1, linked_2)
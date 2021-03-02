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

def filter_even(ll):
    first_node = ll.head
    while (first_node is not None) and (first_node.data % 2 != 0):
        ll.remove_first_node()
        first_node = ll.head
    node = first_node
    while node is not None and node.next is not None:
        if node.next.data % 2 != 0:
            ll.remove_node_after(node)
        else:
            node = node.next
l = LinkedList()
li = [2,11, 4, 8, 5,34, 7, 9, 2, 1, 6]
l.create_list(li)
l.print_list()
filter_even(l)
l.print_list()
# print(type(l.head))
# llist = LinkedList()
# llist.head = Node(1)
# s = Node(2)
# t = Node(3)
# llist.head.next = s
# s.next = t
# llist.print_list()

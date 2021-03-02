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


def mode(lis):
    mode_dictionary = {}
    for value in lis:
        if value not in mode_dictionary:
            mode_dictionary[value] = 1
            continue
        mode_dictionary[value] += 1
    mode = max(mode_dictionary, key=mode_dictionary.get)
    return mode


def mode_linked(linkedlist):
    mode_dictionary = {}
    current = linkedlist.head
    while current is not None:
        value = current.data
        if current.data not in mode_dictionary:
            mode_dictionary[value] = 0
        mode_dictionary[value] += 1
        current = current.next
    mode = max(mode_dictionary, key=mode_dictionary.get)
    return mode


l = [4, 3, 2, 5, 5, 4, 5, 6]
linked = LinkedList()
linked.create_list(l)
linked.print_list()
print(mode_linked(linked))

from data_structures.Node import Node


class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)

    def get_head(self):
        return self.head.get_data()

    def insert_before_head(self, data):
        node = Node(data)

        node.set_next(self.head)
        self.head = node

    def print_list(self):
        string_list = ""
        curr_node = self.head
        while curr_node:
            string_list += " " + str(curr_node.get_data())

            curr_node = curr_node.get_next()

        return string_list

    def insert_end(self, data):
        node = Node(data)

        next_node = self.head.get_next()

        if next_node == None:
            self.head.set_next(data)
        else:
            while next_node:
                if next_node.get_next() is None:
                    break
                next_node = next_node.get_next()
            next_node.set_next(node)

from data_structures.Node import Node


class Queue:
    def __init__(self, data=None):
        self.head = Node(data)

    def enqueue(self, new_value):
        new_node = Node(new_value)

        if self.head == None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node:
                if curr_node.get_next() == None:
                    self.head.set_next(new_node)

                curr_node = curr_node.get_next()

    def dequeue(self):
        if self.head == None:
            return None

        next_node = self.head.get_next()

        if next_node != None:
            self.head = next_node
        else:
            self.head = None

    def peek(self):
        if self.head == None:
            return None

        return self.head.get_data()

class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

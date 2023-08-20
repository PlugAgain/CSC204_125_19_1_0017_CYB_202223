from nodes import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' > ')
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def find_max(self):
        if not self.head:
            return None
        max_data = self.head.data
        current = self.head.next
        while current:
            if current.data > max_data:
                max_data = current.data
            current = current.next
        return max_data
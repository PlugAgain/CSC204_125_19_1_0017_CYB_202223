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

    def find_max_min(self):
        if not self.head:
            return None, None

        current = self.head
        max_data, min_data = current.data, current.data

        while current:
            if current.data > max_data:
                max_data = current.data
            if current.data < min_data:
                min_data = current.data
            current = current.next

        return max_data, min_data
    
    def binary_search(self, target):
        index = 0
        current = self.head
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        return data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=' > ')
            current = current.next
        print("None")

    def sort(self):
        # Insertion sort
        if self.is_empty():
            return

        sorted_queue = Queue()
        while not self.is_empty():
            data = self.dequeue()
            while not sorted_queue.is_empty() and sorted_queue.front.data < data:
                self.enqueue(sorted_queue.dequeue())
            sorted_queue.enqueue(data)

        self.front = sorted_queue.front
        self.rear = sorted_queue.rear

# Testing the linked list operations
if __name__ == "__main__":
    # Binary search on unsorted array
    input_list = [5, 8, 2, 1, 6, 9, 3, 7, 4]
    sll = SingleLinkedList()
    for item in input_list:
        sll.insert(item)

    target = 6
    result = sll.binary_search(target)
    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found")

    #Queue using a single linked list
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()  
    queue.dequeue()
    queue.display()  

    #Sort the queue
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.sort()
    queue.display()  
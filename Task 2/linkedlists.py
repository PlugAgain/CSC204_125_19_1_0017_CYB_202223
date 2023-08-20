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

    def convert_to_bst(self, data_list):
        sorted_list = sorted(data_list)
        self.head = None
        self._convert_to_bst_helper(sorted_list)

    def _convert_to_bst_helper(self, sorted_list):
        if not sorted_list:
            return None

        mid = len(sorted_list) // 2
        root_data = sorted_list[mid]
        root = Node(root_data)
        root.next = self._convert_to_bst_helper(sorted_list[:mid])
        self.head = root
        root.next = self._convert_to_bst_helper(sorted_list[mid + 1:])
        return root

    # Helper method to display the binary search tree (in-order traversal)
    def display_bst(self, node):
        if node:
            self.display_bst(node.next)
            print(node.data, end=' > ')

# Test the linked list operations
if __name__ == "__main__":
    input_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    
    sll = SingleLinkedList()
    for item in input_list:
        sll.insert(item)

    sll.display()

    max_data, min_data = sll.find_max_min()
    print("Maximum:", max_data)
    print("Minimum:", min_data)

    bst_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    bst_sll = SingleLinkedList()
    bst_sll.convert_to_bst(bst_list)
    print("Binary Search Tree:")
    bst_sll.display_bst(bst_sll.head)

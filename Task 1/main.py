from linkedlists import SingleLinkedList

def test_linked_list():
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]

    # Create and test linked list operations
    linked_list = SingleLinkedList()
    for data in data_list:
        linked_list.insert(data)
    print("Original Linked List:")
    linked_list.display()

    max_data = linked_list.find_max()
    print("Maximum value in the linked list:", max_data)

    linked_list.delete(15)
    print("Linked List after deleting 15:")
    linked_list.display()

if __name__ == "__main__":
    test_linked_list()

import time

class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.elements = [None] * capacity

    def insert_at_beginning(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        for i in range(self.size, 0, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[0] = value
        self.size += 1

    def insert_at_end(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.elements[self.size] = value
        self.size += 1

    def remove_at_beginning(self):
        if self.size == 0:
            return None
        value = self.elements[0]
        for i in range(1, self.size):
            self.elements[i - 1] = self.elements[i]
        self.size -= 1
        return value

    def remove_at_end(self):
        if self.size == 0:
            return None
        value = self.elements[self.size - 1]
        self.size -= 1
        return value

    def resize(self, new_capacity):
        new_elements = [None] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_at_beginning(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    def remove_at_end(self):
        if not self.head:
            return None
        current = self.head
        if not current.next:
            self.head = None
            return current.data
        while current.next and current.next.next:
            current = current.next
        value = current.next.data
        current.next = None
        return value


# Test the performance
if __name__ == "__main__":
    array = Array(5)
    linked_list = SinglyLinkedList()

    # Measure time for inserting at the beginning
    start = time.time()
    for i in range(1000):
        array.insert_at_beginning(i)
    end = time.time()
    print(f"Array insert at beginning time: {end - start:.6f} seconds")

    start = time.time()
    for i in range(1000):
        linked_list.insert_at_beginning(i)
    end = time.time()
    print(f"Linked List insert at beginning time: {end - start:.6f} seconds")

    # Measure time for inserting at the end
    start = time.time()
    for i in range(1000):
        array.insert_at_end(i)
    end = time.time()
    print(f"Array insert at end time: {end - start:.6f} seconds")

    start = time.time()
    for i in range(1000):
        linked_list.insert_at_end(i)
    end = time.time()
    print(f"Linked List insert at end time: {end - start:.6f} seconds")

    # Measure time for removing at the beginning
    start = time.time()
    for i in range(1000):
        array.remove_at_beginning()
    end = time.time()
    print(f"Array remove at beginning time: {end - start:.6f} seconds")

    start = time.time()
    for i in range(1000):
        linked_list.remove_at_beginning()
    end = time.time()
    print(f"Linked List remove at beginning time: {end - start:.6f} seconds")

    # Measure time for removing at the end
    start = time.time()
    for i in range(1000):
        array.remove_at_end()
    end = time.time()
    print(f"Array remove at end time: {end - start:.6f} seconds")

    start = time.time()
    for i in range(1000):
        linked_list.remove_at_end()
    end = time.time()
    print(f"Linked List remove at end time: {end - start:.6f} seconds")


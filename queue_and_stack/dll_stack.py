import sys

from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(None)
    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if not self.size:
            return
        value = self.storage.head.value
        self.storage.remove_from_head()
        self.size -= 1
        return value

    def len(self):
        return len(self.storage)

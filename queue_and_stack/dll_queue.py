
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(None)

    def enqueue(self, value):
        self.storage.add_to_head(value)
        print(self.storage.head.value)

    def dequeue(self):
        if not self.storage.tail:
            return 
        value = self.storage.tail.value
        self.storage.remove_from_tail()
        return value

    def len(self):
        return self.storage.length

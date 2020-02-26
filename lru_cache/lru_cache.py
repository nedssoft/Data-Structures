from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.storage = dict()
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def __len__(self):
        return len(self.storage)

    def get(self, key):
        
        # If the key is not in storage return None
        if not key in self.storage:
            return None
        else:

            # Move the node to the tail as lest recently used
           node = self.storage[key]
           self.dll.move_to_end(node)
            # Return value
           return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
       
       # Check if key is already in storage
       if key in self.storage:
           # Overwrite it with the new value
           node = self.storage[key]
           node.value = (key, value)
           # Move it to the end
           self.dll.move_to_end(node)

        # Else check if the limit is reached
       elif len(self) == self.limit:
            head = self.dll.head

            # Delete the head node from the storage
            del self.storage[head.value[0]]

            # Remove from the List
            self.dll.remove_from_head()
            
            # Add the new value to the tail
            self.dll.add_to_tail((key, value))

            # Store the new node in the cache
            self.storage[key] = self.dll.tail
       else:

           # Add to tail
           self.dll.add_to_tail((key, value))

                # Store the new node in the cache
           self.storage[key] = self.dll.tail



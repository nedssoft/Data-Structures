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
        self.storage = DoublyLinkedList()
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
        if not len(self.storage):
            return None
        current_node = self.storage.head

        # Set the value to None
        value = None
        while current_node:
            if key in current_node.value:
                value = current_node.value[key]
                # Move current node to the end
                self.storage.move_to_end(current_node)
                break
            current_node = current_node.next
        return value

    def has_key(self, key):
        if not len(self.storage):
            return None
        current_node = self.storage.head
        # Set the value to None
        has_attr =  None
        while current_node:
            # Check if any of the nodes has the given key
            if key in current_node.value:
                # If the key exists, return the node
                has_attr = current_node
                break
            current_node = current_node.next
        return has_attr
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
        # Check if the key already exists
        node_with_existing_key = self.has_key(key)

        if (node_with_existing_key):
            # update the value
            node_with_existing_key.value[key] = value
            # move it to the end of the cache
            self.storage.move_to_end(node_with_existing_key)
        elif len(self) >= self.limit:
            # Remove the oldest
            self.storage.remove_from_head()
            # Add the item to the tail of the cache
            self.add_dic_to_cache(key, value)
        else:
            # Add the item to the tail of the cache
            self.add_dic_to_cache(key, value)

    def add_dic_to_cache(self, key, value):
        dic = dict()
        dic[key] = value
        self.storage.add_to_tail(dic)


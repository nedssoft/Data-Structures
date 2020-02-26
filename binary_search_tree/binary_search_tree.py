import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
          # LEFT CASE
        # check if our new nodes value is less than the current nodes value
        if value < self.value:
            # does it have a child to the left?
            if self.left is not None:
                self.left.insert(value)
                # place our new node here
            # otherwise
            else:
                self.left = BinarySearchTree(value)
                # repeat process for the left

        # RIGHT CASE
        
        # check if the new nodes value is greater than or equal to the current nodes value
        if value >= self.value:
            # does it have a child to the right?
            if self.right is not None:
                self.right.insert(value)
                # place our new node here
            # otherwise
            else:
                self.right = BinarySearchTree(value)
                # repeat the process for the right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        current_value = self.value
        if current_value == target:
            return True
        
        # Check if the target is less than the current node value
        if target < current_value:

            # Check if left is not None
            if self.left is not None:

                # Repeat the process towards the left
                return self.left.contains(target)
            else:

                # It means the target is not at the left
                return False

        # Let's search the right
        if target >= current_value:

            # Check if the right is none
            if self.right is None:

                # Then it is not at the right
                return False
            else:
                return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

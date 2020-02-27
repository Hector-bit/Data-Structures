# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #if the tree is empty
        print(value, self.value, 'value then self.value')
        if self.value == None:
            #make the value a root node
            BinarySearchTree(value)
        #if the tree is not empty
        if self.value != None:
            #if the value is < to the root
            if value < self.value:
                #place value to the left
                self.left == BinarySearchTree(value)
            #if the value is > to the root
            if value > self.value:
                #place value to the right
                self.right == BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if root = target 
            #return true
        #if target is < root
            #go left and check that node
        #if target is > root
            #go right and check that node
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        #go right until you can't go right anymore and return that node
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

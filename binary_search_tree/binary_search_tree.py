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
        #if the self.value is empty
        if self.value == None:
            #make the value a root node
            BinarySearchTree(value)
        #if the tree is not empty
        if self.value != None:
            #if the value is < to the root
            if value < self.value:
                #place value to the left
                if self.left == None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
                return
            #if the value is > to the root
            if value > self.value:
                #place value to the right
                if self.right == None:
                    self.right = BinarySearchTree(value)
                else:
                    # self.right == BinarySearchTree(value)
                    self.right.insert(value)
                return


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        print(self.value, 'AASDF PQWER', target)
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)
            if target > self.value:
                print(self.right, 'RIGHTSIDEVALUE')
                if self.right == None:
                    print('BIGOLDESUPERFALSE')
                    return False
                else:
                    return self.right.contains(target)

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

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.size += 1
        if self.top is None: 
            self.top = DoublyLinkedList(value) 
        else: 
            new_node = DoublyLinkedList(value) 
            self.top.tail = new_node 
            new_node.head = self.top 
            new_node.tail = None
            self.top = new_node 

    def pop(self):
        if self.top is None: 
            return None
        else: 
            temp = self.top 
            self.top = self.top.head
            self.top.prev = None
            self.size -= 1
            return temp 

    def len(self):
        return self.size

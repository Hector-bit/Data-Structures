import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.front = None
        self.back = None

    def enqueue(self, value):
        if self.back == None:
            self.front = DoublyLinkedList(value)
            self.back = self.front
        else: 
            self.back.next = DoublyLinkedList(value) 
            self.back.next.prev = self.back 
            self.back = self.back.next

    def dequeue(self):
        if self.front is None: 
            return None
        else: 
            temp= self.front.data 
            self.front = self.front.next
            self.front.prev=None
            return temp 

    def len(self):
        temp=self.front 
        count=0
        while temp is not None: 
            count=count+1
            temp=temp.next
        return count 

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
        print(value, 'this is value')
        if self.back is None: 
            self.head = DoublyLinkedList(value) 
            self.back = self.head 
        else: 
            self.back.next = DoublyLinkedList(value) 
            self.back.next.prev = self.back 
            self.back = self.back.next

    def dequeue(self):
        if self.front is None: 
            return None
        else: 
            temp= self.front.value 
            self.front = self.front.next
            self.front.prev = None
            return temp 

    def len(self):
        temp = self.front 
        count=0
        while temp != None: 
            count=count+1
            temp=temp.next
        return count 

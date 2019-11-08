# from doubly_linked_list import DoublyLinkedList
import sys
# sys.path.append('../doubly_linked_list')
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../doubly_linked_list'))
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if(self.storage.length > 0):
            self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size

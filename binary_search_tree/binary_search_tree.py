import sys
import os
# sys.path.append('../queue_and_stack')
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../queue_and_stack'))
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
    # Insert the given value into the tree
    def insert(self, value):
        # we have two have the one used to initial the class
        # and the one passed to the insert method
        if value <= self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        return 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # set the max to the value
        # move through the right node
        # why dont we have an maxValue we compare with 
        if self.value is None:
            return None
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

        # we have the iterative one which is similar to the way i was thinking
        # max_value = self.value
        # current = self
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
                # check if the value is not none
        if self.value != None:
            # Call cb and pass the current value
            cb(self.value)
            # if the left of the current node is not None
            if self.left != None:
                # Call the for_each method on the left node passing the cb
                self.left.for_each(cb)
            # if the right of the current node is not None
            if self.right != None:
                # Call the for_each method on the right node passing the cb
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal DFT RECUSSION
    def in_order_print(self, node):
        # left node right
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        # if right, right.in_order_dft
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.len() > 0:
            d = q.dequeue()
            print(d.value)
            # how does it move up with out the set and visited
            # set/visited is not needed its not a graph
            if d.left != None:
                # forget about every thing outside of the while loop
                # don't forget its just a loop
                # as u are enqueuing it get the oldest to work on
                q.enqueue(d.left)
            if d.right != None:
                q.enqueue(d.right)

# pre-order
# root left right

# post-order
# left right root

# in order
# left root right

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # depth first ta
    def dft_print(self, node):
        # use a stack data structure
        s = Stack()
        # push the starting node on to the stack
        # loop while the stack has data
            # pop the current it em off the stack
            # print the current value
            # if the current node has a left child
                # push the left child on to the stack
            # if the current node has a right child
                # push right child on to the stack          
        # visited = set()
        s.push(node)
        while s.len():
            d = s.pop()
            print(d.value)
            # u move left till u get to the end
            # u then pop 
            if d.left != None:
                s.push(d.left)
            if d.right != None:
                s.push(d.right)
        # the youtube guy used recussion
        # self.dft_print(d.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
        # dont understand how does node.left.post_order_dft
        # it worked but dont know how
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)





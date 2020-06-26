from queue import Queue
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
                return True

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree

    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        if self:
            fn(self.value)
            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # create a queue for nodes
        queue = Queue()
        # add first node to queue
        queue.enqueue(node)
        # while queue isn't empty
        while queue.len() != 0:
            # remove the first node from the queue
            popped = queue.dequeue()
            # print the removed node
            print(popped.value)
            # add the children into the queue
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create stack for nodes
        stack = Stack()
        # add the first node to stack
        stack.push(node)

        # while the stack isn't empty
        while stack.len() != 0:
            # get the current node from the top
            current = stack.pop()

            print(current.value)

            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)

        # Stretch Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)

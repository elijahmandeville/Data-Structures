class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None  # stores a node that corresponds to our first node in the list
        self.tail = None  # stores a node that is the end of list

    def add_to_head(self, value):
        # create node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            # point the node at current tail to new node
            self.tail.next_node = new_node
            self.tail = new_node

    # Remove head and return value
    def remove_head(self):
        # If list is empty, do nothing
        if not self.head:
            return None

        # If list has one element, set tail and head to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # if we have more elements
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node till we see the value, or can't loop no mo'
        current_node = self.head

        while current_node is not None:
            # check if this is the node we're looking for
            if current_node.value == value:
                return True

            # Otherwise, go to next node
            current_node = current_node.next_node
        return False

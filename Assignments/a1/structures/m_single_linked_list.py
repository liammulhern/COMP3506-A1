"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will be used for marking.
"""


class SingleNode:
    """
    This is the Node object; it contains data and a next pointer
    """

    def __init__(self, data):
        """
        We can init the object with some data, but the next pointer
        is initially set to None
        """
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next SingleNode

    # Some convenience functions for the SingleNode structure
    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def set_next(self, node):
        self._next = node

    def get_next(self):
        return self._next

class SingleLinkedList:
    """
    Task 1.1: This is a singly linked list sample implementation, but it
    contains two bugs. You should find them and fix them before proceeding!
    You should write tests in test_structures.py to see if you can find out
    what the bugs are.
    """

    def __init__(self):
        """
        Initialize with no nodes and a size of zero
        """
        self._head = None
        self._size = 0

    # We can convert the list to a string by overriding the __str__ builtin
    def __str__(self):
        string_rep = ""
        cur = self.get_head()
        while cur is not None:
            # Assumes the data stored in cur has __str__ implemented
            string_rep += str(cur.get_data()) + " -> "
            cur = cur.get_next()
        string_rep += "[EOL]"  # end of list == None
        return string_rep

    # Delete all of the elements in the list one-by-one. This is essentially
    # a simulation, as with Python's memory management, we only need to remove
    # reference to self._head to "delete" the linked list.
    def traverse_and_delete(self):
        cur = self.get_head()
        while cur is not None:
            # Get a handle on the next node
            nex = cur.get_next()
            # Delete the reference to the next node
            cur.set_next(None)
            # Delete the data
            cur.set_data(None)
            # Move forward
            cur = nex
        # Don't forget to remove the ref to the head node
        self._head = None
        # And reset the size
        self._size = 0

    # Return the number of elements stored in the linked list
    def get_size(self):
        return self._size

    # Set a new size
    def set_size(self, s):
        self._size = s

    # Return the head element
    def get_head(self):
        return self._head

    # Set a new head
    def set_head(self, node):
        self._head = node

    # Insert a node to the front of the list
    def insert_to_front(self, node):
        if self._head is not None:
            node.set_next(self._head)
        self._head = node

    # Insert a node to the back of the list
    def insert_to_back(self, node):
        cur = self.get_head()
        # Check corner case; the head is yet to be set
        if cur is None:
            self._size += 1
            return

        # Keep going until the next of the current node is empty
        while cur.get_next() is not None:
            cur = cur.get_next()
        # We are now on the last valid node, let's insert
        cur.set_next(node)
        self._size += 1

    # Remove a node from the front of the list and return it
    def remove_from_front(self):
        if self._size == 0:
            return None
        node = self.get_head()
        self._head = node.get_next()
        self._size -= 1
        return node

    # Remove a node from the back of the list and return it
    def remove_from_back(self):
        # Nothing to remove
        if self._size == 0:
            return None
        # Just the head element
        if self._size == 1:
            cur = self.get_head()
            self.set_head(None)
            self._size -= 1
            return cur
        # More than one element - let's walk the list
        prev = None
        cur = self.get_head()
        # Keep going until the next of the current node is empty
        while cur.get_next() is not None:
            prev = cur
            cur = cur.get_next()
        prev.set_next(None)
        # We are now on the last valid node, let's insert
        self._size -= 1 
        return cur

    # Find an element and return it if it exists, return None otherwise
    def find_element(self, elem):
        cur = self.get_head()
        while cur is not None:
            if cur.get_data() == elem:
                return cur
            cur = cur.get_next()
        return None

    # Remove and return the first instance of an element if found
    def find_and_remove_element(self, elem):
        prev = self.get_head()
        # Empty list - nothing to do
        if prev == None:
            return None
        cur = prev.get_next()
        # Corner case: if prev (head) is the element, we need to fix the head ptr
        if prev.get_data() == elem:
            self._head = cur
            self._size -= 1
            return prev 

        # Walk the list
        while cur is not None:
            # We found it - move the previous ptr to the current next
            if cur.get_data() == elem:
                prev.set_next(cur.get_next())
                self._size -= 1
                return cur
            
            # Keep moving forward otherwise
            prev = cur
            cur = cur.get_next()
        return None

    # Reverse a linked list
    def reverse(self):
        if self.get_head() is None:
            return
        if self.get_head().get_next() is None:
            return
        cur = self.get_head()
        nex = cur.get_next()
        cur.set_next(None)
        while nex is not None:
            follow = nex.get_next()
            nex.set_next(cur)
            cur = nex
            nex = follow

        self.set_head(cur)

"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will be used for marking.
"""

# Import the supporting data structures
from structures.m_extensible_list import ExtensibleList
from structures.m_single_linked_list import SingleLinkedList, SingleNode

class EStack(ExtensibleList):
    """
    A simple stack implementation that uses the ExtensibleList implemented in
    m_extensible_list.py to provide last-in-first-out (LIFO) operations
    """
    
    # Constructor
    def __init__(self):
        """
        Create an empty stack
        """
        super().__init__()

    # Think carefully about which operations inherited from the ExtensibleList
    # need to be overridden to allow the Stack to function correctly. Implement
    # those below; you can add any other functions as necessary. Note that it
    # is totally OK to implement push/pop/peek in terms of existing functionality
    # inherited from the ExtensibleList

    def push(self, elem):
        """
        Push a new element (elem) to the top of the stack
        """
        self.append(elem)

    def pop(self):
        """
        Remove and return the top element, return None if empty
        """
        return self.remove_at(self._size - 1) 

    def peek(self):
        """
        Peek at the top element, but do not pop it out, return None if empty
        """
        return self._data[self._size - 1]

    def empty(self):
        """
        Boolean helper: Returns True if the stack is empty, False otherwise
        """
        return self._size == 0

    def reset(self):
        raise Exception("Not Implemented In Stack")
   
    def __setitem__(self):
        raise Exception("Not Implemented In Stack")

    def set_at(self):
        raise Exception("Not Implemented In Stack")

    def remove(self, element):
        raise Exception("Not Implemented In Stack")

    def is_empty(self):
        raise Exception("Not Implemented In Stack")

    def is_full(self):
        raise Exception("Not Implemented In Stack")

    def get_size(self):
        raise Exception("Not Implemented In Stack")

    def get_capacity(self):
        raise Exception("Not Implemented In Stack")

class LStack(SingleLinkedList):
 
    """
    Another simple stack implementation. This one uses the SingleLinkedList
    instead of the ExtensibleList for object storage
    """

    # Constructor
    def __init__(self):
        """
        Create an empty stack
        """
        super().__init__()

    # Think carefully about which operations inherited from the SingleLinkedList
    # need to be overridden to allow the Stack to function correctly. Implement
    # those below; you can add any other functions as necessary. Note that it
    # is totally OK to implement push/pop/peek in terms of existing functionality
    # inherited from the SingleLinkedList

    def push(self, elem):
        """
        Push a new element (elem) to the top of the stack
        """
        element_node = SingleNode(elem)

        self.insert_to_front(element_node)

    def pop(self):
        """
        Remove and return the top element, return None if empty
        """
        element_node: SingleNode = self.remove_from_front()
        
        if element_node == None:
            return None

        return element_node.get_data()

    def peek(self):
        """
        Peek at the top element, but do not pop it out, return None if empty
        """
        element_node: SingleNode = self.get_head()
        
        if element_node == None:
            return None

        return element_node.get_data()

    def empty(self):
        """
        Boolean helper: Returns True if the stack is empty, False otherwise
        """
        return self._size == 0

    def traverse_and_delete(self):
        raise Exception("Not Implemented In Stack")
   
    def get_size(self):
        raise Exception("Not Implemented In Stack")

    def set_size(self, s):
        raise Exception("Not Implemented In Stack")

    def set_head(self):
        raise Exception("Not Implemented In Stack")
    
    def insert_to_back(self, node):
        raise Exception("Not Implemented In Stack")

    def remove_from_back(self):
        raise Exception("Not Implemented In Stack")

    def find_element(self, elem):
        raise Exception("Not Implemented In Stack")

    def find_and_remove_element(self, elem):
        raise Exception("Not Implemented In Stack")

    def reverse(self):
        raise Exception("Not Implemented In Stack")

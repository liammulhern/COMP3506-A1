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
        pass

    # Think carefully about which operations inherited from the ExtensibleList
    # need to be overridden to allow the Stack to function correctly. Implement
    # those below; you can add any other functions as necessary. Note that it
    # is totally OK to implement push/pop/peek in terms of existing functionality
    # inherited from the ExtensibleList

    def push(self, elem):
        """
        Push a new element (elem) to the top of the stack
        """
        pass

    def pop(self):
        """
        Remove and return the top element, return None if empty
        """
        pass

    def peek(self):
        """
        Peek at the top element, but do not pop it out, return None if empty
        """
        pass

    def empty(self):
        """
        Boolean helper: Returns True if the stack is empty, False otherwise
        """
        return True


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
        pass

    # Think carefully about which operations inherited from the SingleLinkedList
    # need to be overridden to allow the Stack to function correctly. Implement
    # those below; you can add any other functions as necessary. Note that it
    # is totally OK to implement push/pop/peek in terms of existing functionality
    # inherited from the SingleLinkedList

    def push(self, elem):
        """
        Push a new element (elem) to the top of the stack
        """
        pass

    def pop(self):
        """
        Remove and return the top element, return None if empty
        """
        pass

    def peek(self):
        """
        Peek at the top element, but do not pop it out, return None if empty
        """
        pass

    def empty(self):
        """
        Boolean helper: Returns True if the stack is empty, False otherwise
        """
        return True

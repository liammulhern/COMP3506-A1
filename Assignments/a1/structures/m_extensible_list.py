"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will be used for marking.
"""

class ExtensibleList:
    """
    A simple extensible list implementation that uses a contiguous slab of data
    to maintain the elements inside. You may allow the list to have some small
    initial capacity like 4, 8 or 16 elements
    Note that the list capacity only automatically grows; it does not need
    to automatically shrink
    """

    def __init__(self):
        """
        Store your data in _data - you may edit that line if desired
        You may also add any other member variables you might need here
        in the constructor
        """
        self._data = [None] * 4 # [None, None, None, None] (space for 4 items)
        # Add any other member variables you might need below

    def __str__(self):
        """
        Stringify the list. Don't forget to show the empty cells
        """
        pass

    def __resize(self):
        """
        Increases the list size; does not need to handle shrinking.
        """
        pass

    def reset(self):
        """
        Reset the list to its initial form, including the capacity. 
        """
        pass

    def __getitem__(self, index):
        """
        This function implements array-like access
        That is, we will be able to return the element at _data[index]
        if it exists; an exception will be thrown otherwise. You may assume
        the index is always valid (no need to check the bounds)
        """
        pass

    def get_at(self, index):
        """
        Return an element at a given index; same as __getitem__, but it will
        also check that the index is within the desired bounds;
        if out of bounds, return None
        """
        pass

    def __setitem__(self, index, element):
        """
        This is the set version if __getitem__ that allows us to set the
        value of _data[index] to element; similarly, you do not need to
        do any bounds checking here
        """
        pass

    def set_at(self, index, element):
        """
        Overwrite or set the value at a given index; same as __setitem__, but
        it will also check that the index is within the desired bounds;
        if out of bounds, do nothing
        """
        pass

    def append(self, element):
        """
        Add an element to the end of the list (after the last existing element)
        You should resize (grow) the list if necessary
        """
        pass

    def remove(self, element):
        """
        Remove the first element with the specified value
        Don't forget to clean up the items ahead of the deletion point
        You do not need to shrink the capacity
        EG: Given [1, 2, 3, None] and calling remove(2) should result in
        a list [1, 3, None, None], not [1, None, 3, None]. Elements
        should remain contiguous.
        """
        pass

    def remove_at(self, index):
        """
        Remove and return the element at a given index; make sure the bounds
        are checked. If out of bounds, return None
        """
        pass

    def is_empty(self):
        """
        Boolean helper to tell us if the structure is empty or not
        """
        pass

    def is_full(self):
        """
        Boolean helper to tell us if the structure is full or not
        "Full" means there are no empty cells in the array
        """
        pass

    def get_size(self):
        """
        Return the number of non-empty elements in the list
        """
        pass

    def get_capacity(self):
        """
        Return the total capacity (the number of slots) of the list
        """
        pass


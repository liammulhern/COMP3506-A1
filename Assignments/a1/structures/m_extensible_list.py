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
        self._size = 0
        self._capacity = 4

    def __str__(self):
        """
        Stringify the list. Don't forget to show the empty cells
        """
        string_rep = ""

        for i in range(0, self._capacity):
            # Get string representation of data and add to output
            string_rep += str(self._data[i])

            # Add comma if data is not the last element
            if i < (self._capacity - 1):
                string_rep += ", "

        return string_rep

    def __resize(self):
        """
        Increases the list size; does not need to handle shrinking.
        """
        # Double the size of the list 
        new_capacity = self._capacity * 2
        resized_data = [None] * new_capacity 

        # Copy old data to new slab of memory
        for i in range(0, self._size):
            resized_data[i] = self._data[i]

        self._capacity = new_capacity
        self._data = resized_data

    def reset(self):
        """
        Reset the list to its initial form, including the capacity. 
        """
        self._data = [None] * 4
        self._size = 0
        self._capacity = 4

    def __getitem__(self, index):
        """
        This function implements array-like access
        That is, we will be able to return the element at _data[index]
        if it exists; an exception will be thrown otherwise. You may assume
        the index is always valid (no need to check the bounds)
        """
        if self._data[index] is None:
            raise Exception("Index Error") 

        return self._data[index]

    def get_at(self, index):
        """
        Return an element at a given index; same as __getitem__, but it will
        also check that the index is within the desired bounds;
        if out of bounds, return None
        """
        if self._size == 0:
            return None

        if index < 0 or index >= self._size:
            return None

        return self.__getitem__(index)

    def __setitem__(self, index, element):
        """
        This is the set version if __getitem__ that allows us to set the
        value of _data[index] to element; similarly, you do not need to
        do any bounds checking here
        """
        if self._data[index] == None:
            self._size += 1 

        self._data[index] = element

    def set_at(self, index, element):
        """
        Overwrite or set the value at a given index; same as __setitem__, but
        it will also check that the index is within the desired bounds;
        if out of bounds, do nothing
        """
        if self._size == 0:
            return
        elif index < 0 or index >= self._size:
            return

        self.__setitem__(index, element)

    def append(self, element):
        """
        Add an element to the end of the list (after the last existing element)
        You should resize (grow) the list if necessary
        """
        if self._capacity <= self._size:
            self.__resize()

        self._data[self._size] = element
        self._size += 1

    def remove(self, element):
        """
        Remove the first element with the specified value
        Don't forget to clean up the items ahead of the deletion point
        You do not need to shrink the capacity
        EG: Given [1, 2, 3, None] and calling remove(2) should result in
        a list [1, 3, None, None], not [1, None, 3, None]. Elements
        should remain contiguous.
        """
        if self._size == 0:
            return None

        # Set deletion point default to -1 (invalid index)
        deletion_point = -1
        removed_elem = None

        for i in range(self._size):
            if self._data[i] == element and deletion_point == -1:
               # When element is found set the deletion point to the 
               # current index 
               deletion_point = i
               removed_elem = self._data[i]
               self._data[i] = None
               self._size -= 1
            elif deletion_point != -1:
                # Move data back 1 after the deletion
                self._data[i - 1] = self._data[i]
                self._data[i] = None

        return removed_elem

    def remove_at(self, index):
        """
        Remove and return the element at a given index; make sure the bounds
        are checked. If out of bounds, return None
        """
        if self._size == 0:
            return None

        if self.get_at(index) == None:
            return None

        # Remove data at index
        removed_elem = self._data[index] 
        self._data[index] = None

        for i in range(index + 1, self._size):
            # Move data back 1 after the deletion
            self._data[i - 1] = self._data[i]
            self._data[i] = None

        self._size -= 1

        return removed_elem

    def is_empty(self):
        """
        Boolean helper to tell us if the structure is empty or not
        """
        return self._size == 0

    def is_full(self):
        """
        Boolean helper to tell us if the structure is full or not
        "Full" means there are no empty cells in the array
        """
        return self._size == self._capacity

    def get_size(self):
        """
        Return the number of non-empty elements in the list
        """
        return self._size

    def get_capacity(self):
        """
        Return the total capacity (the number of slots) of the list
        """
        return self._capacity


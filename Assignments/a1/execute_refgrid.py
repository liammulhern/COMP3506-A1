"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will be used for marking.
"""

# Import helper libraries
import sys
import argparse
import time

# Import our data structures
from structures.m_extensible_list import ExtensibleList
from structures.m_stack import EStack, LStack
from structures.m_single_linked_list import SingleLinkedList, SingleNode

class RefGrid:
    """
    You may add fields to this structure, but you must use either the
    provided ExtensibleList or SingleLinkedList member functions to
    store and operate on your RefGrid. You may use other data structures
    within each function where necessary.
    """

    def __init__(self):
        """
        Data is stored in either linkedlist or extlist depending on which
        read_to_* function is called.
        """
        self.linkedlist = SingleLinkedList()
        self.extlist = ExtensibleList()
        # Initial rows and length counts
        self.rows = 0
        self.len = 0

    def read_to_linkedlist(self, input_file):
        """
        DO NOT MODIFY.
        Reads a refgrid file into a linked list.
        Assumes you have completed Task 1.1.
        """
        with open(input_file) as f:
            first = True
            for line in f:
                self.rows += 1
                for character in line.strip():
                    self.linkedlist.insert_to_front(SingleNode(character))
                    if first:
                        self.len += 1
                first = False
        self.linkedlist.reverse()

    def read_to_extlist(self, input_file):
        """
        DO NOT MODIFY.
        Reads a refgrid file into an extensible list.
        Assumes you have completed Task 1.2 and, in particular, the append func.
        """
        with open(input_file) as f:
            first = True
            for line in f:
                self.rows += 1
                for character in line.strip():
                    self.extlist.append(character)
                    if first:
                        self.len += 1
                first = False

    def stringify_linkedlist(self):
        """
        Converts the linked list to a string; used for printing the RefGrid
        """
        outstr = ""
        counter = 0
        cur = self.linkedlist.get_head()
        while cur != None:
            outstr += str(cur.get_data())
            counter += 1
            if counter % self.len == 0:
                outstr += "\n"
            cur = cur.get_next()
        return outstr

    def stringify_extlist(self):
        """
        Converts the extensible list to a string; used for printing ...
        """
        pass

    def stringify_spliced_linkedlist(self):
        """
        Converts a cut-and-spliced linked list by handling the variable row length
        of each sequence; use this to test your output for Task 2.2.
        """
        pass

    def reverse_seq(self, k):
        """
        Task 2.1, sequence reversal. You need to use/store your result in the
        linkedlist class member.
        """
        pass


    def cut_and_splice(self, pattern, plen, target, tlen):
        """
        Task 2.2, cut-and-splice (plen is the length of the pattern, tlen is
        the length of the target. We provide these so you don't have to call
        len() since it's not allowed...
        Note: You are allowed to access and operate on the strings directly,
        EG: first_char = pattern[0] - you do NOT need to convert them to
        linked list or extensible list representations
        """
        pass

    # Barry's left and below helper functions
    def right(self, idx):
        """
        Return the index to the right of idx or 0 if it does not exist (if it
        is out of bounds)
        """
        pass

    def below(self, idx):
        """
        Return the index below idx or 0 if it does not exists (is out of bounds)
        """
        pass

    def is_viable(self):
        """
        Task 2.3, cloning viability
        No need to modify data here, just return True or False
        Make sure you use self.extlist for this task based on Barry's algorithm
        from the assignment specification
        """
        pass


def validate_patterns(p, t):
    """
    Helper to validate the pattern from a command line input. Makes sure you
    do not accidentally pass in illegal patterns or targets
    """
    if len(p) <= 0 or len(p) > 4:
        print("Error: Pattern [" + p + "] is too short or too long.")
        return False
    if len(t) <= 0 or len(t) > 4:
        print("Error: Target [" + t + "] is too short or too long.")
        return False
    bases = ["a", "c", "g", "t"]
    for b in bases:
        if p.count(b) > 1 or t.count(b) > 1:
            print("Error: Only allowed one occurrences of each base.")
            return False
        p = p.replace(b, "")
        t = t.replace(b, "")
    if len(p) > 0 or len(t) > 0:
        print("Error: Illegal characters provided.")
        return False
    return True


if __name__ == "__main__":

    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(
        description="COMP3506/7505 Assignment One: DNA-RefGrid"
    )
    parser.add_argument(
        "--refgrid",
        type=str,
        required=True,
        help="Path to refgrid file"
    )
    parser.add_argument(
        "--reverse-k",
        type=int,
        help="Reverse the k-th sequence."
    )
    parser.add_argument(
        "--cut-and-splice",
        type=str,
        help="Cut and splice pattern P with T. Use format P:T (eg: --cut-and-splice gta:atcgc"
    )
    parser.add_argument(
        "--check-clone",
        action="store_true",
        help="Check if the RefGrid is viable for cloning."
    )
    args = parser.parse_args()
    
    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # The RefGrid object that we will operate on
    my_refgrid = RefGrid()

    # Note that the three calls below are independent; each specific task will
    # eventuate in a sys.exit(0) call which means you DO NOT need to handle a
    # situation where a refgrid is reversed, then cut_and_splice'd, and then
    # has the cloning viability checked. That is, each of Task 2.1, 2.2, and
    # 2.3 will be tested in isolation.

    # Task 2.1: Reverse-k
    if args.reverse_k is not None:
        print("Testing reverse k with k = ", args.reverse_k)
        # Read the refgrid to a linked list
        my_refgrid.read_to_linkedlist(args.refgrid)
        my_refgrid.reverse_seq(args.reverse_k)
        print(my_refgrid.stringify_linkedlist(), end="")
        sys.exit(0)

    # Task 2.2 Cut and Splice
    if args.cut_and_splice is not None:
        # Yes, I am allowed to use .split, sorry :-)
        pattern, target = args.cut_and_splice.split(":")
        # Validate the pattern
        if not validate_patterns(pattern, target):
            sys.exit(-1)
        print("Testing cut-and-splice with P = ", pattern, "and T = ", target)
        # Read the refgrid to a linked list
        my_refgrid.read_to_linkedlist(args.refgrid)
        # We supply the pattern length for your information
        my_refgrid.cut_and_splice(pattern, len(pattern), target, len(target))
        print(my_refgrid.stringify_spliced_linkedlist(), end="")
        sys.exit(0)

    # Task 2.3 Cloning Viability
    if args.check_clone:
        # This time, we will use the extlist to store the data
        # based on Barry Malloc's implementation
        my_refgrid.read_to_extlist(args.refgrid)
        is_viable = my_refgrid.is_viable()
        print("Testing viability via L-Path: ", is_viable)
        sys.exit(0)


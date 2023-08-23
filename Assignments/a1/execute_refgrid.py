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
        outstr = ""
        
        for i in range(self.extlist.get_size()):
            outstr += str(self.extlist[i])

            if i < self.extlist.get_size() - 1:
                outstr += ", "

        return outstr

    def stringify_spliced_linkedlist(self):
        """
        Converts a cut-and-spliced linked list by handling the variable row length
        of each sequence; use this to test your output for Task 2.2.
        """
        outstr = ""
        base_count = 0
        strand_count = 0
        strand_count_max = self.extlist.get_size() 
        current_base = self.linkedlist.get_head()

        while current_base != None:
            outstr += str(current_base.get_data())
            base_count += 1
            
            if base_count % self.extlist[strand_count] == 0:
                outstr += "\n"
                base_count = 0
                if strand_count < strand_count_max - 1:
                    strand_count += 1

            current_base = current_base.get_next()

        return outstr

    def reverse_seq(self, k):
        """
        Task 2.1, sequence reversal. You need to use/store your result in the
        linkedlist class member.

        Total Time Complexitiy: O(m) + O(p) + O(q) = O(m + p + q) => O(n)
        """
        max_k = (self.linkedlist.get_size() // self.len) - 1

        if k < 0 or k > max_k: 
            return

        strand_start_index = k * self.len
        reversed_sequence: LStack = LStack()

        # Get node at the start of the strand sequence 
        # Complexitiy: O(m)
        start_strand: SingleNode = self._linked_list_go_to_index(strand_start_index)
        cur: SingleNode = start_strand

        # Create stack of strand bases
        # Complexitiy: O(p)
        for i in range(self.len):
            strand = cur.get_data()
            reversed_sequence.push(strand)
            cur = cur.get_next()

        cur = start_strand

        # Insert reversed strand sequence as the strand
        # Complexitiy: O(q)
        for i in range(self.len):
            # Get strand base from top of stack and replace
            # the current strand base
            strand = reversed_sequence.pop()
            cur.set_data(strand)
            cur = cur.get_next()
    
    def _linked_list_go_to_index(self, index) -> SingleNode:
        """
        Get the list node at the specified index in the linked list.
        """
        cur: SingleNode = self.linkedlist.get_head()

        # Go to start index of strand in linked list
        for i in range(index):
            cur = cur.get_next()

        return cur

    def cut_and_splice(self, pattern, plen, target, tlen):
        """
        Task 2.2, cut-and-splice (plen is the length of the pattern, tlen is
        the length of the target). We provide these so you don't have to call
        len() since it's not allowed...
        Note: You are allowed to access and operate on the strings directly,
        EG: first_char = pattern[0] - you do NOT need to convert them to
        linked list or extensible list representations
        """
        max_strand_squence = self.linkedlist.get_size() // self.len 

        current_base_node: SingleNode = self.linkedlist.get_head()
        base_pattern_start_node = current_base_node
        index = 0

        # Iterate over the number of strand squences
        # O(n/len)
        for current_strand_sequence in range(max_strand_squence):
            current_strand_length = self.len
            current_base_index = 0
            similar_bases = 0
            base_pattern_start_index = index

            # Iterate over the bases in the strand sequence
            # O(len)
            while current_base_index < self.len:
                base = current_base_node.get_data()

                # Check for pattern match
                if base == pattern[similar_bases]:
                    similar_bases += 1
                    if similar_bases == 1:
                        base_pattern_start_index = index
                        base_pattern_start_node = current_base_node
                elif base == pattern[0]:
                    similar_bases = 1
                    base_pattern_start_index = index
                else:
                    similar_bases = 0
                    base_pattern_start_node = current_base_node
                    base_pattern_start_index = index

                # Save pointer to end of list pattern in case we insert
                base_pattern_end_node: SingleNode = current_base_node.get_next()

                if similar_bases == plen:
                    # Pattern matches start inserting new base target nodes
                    current_base_target_node: SingleNode = base_pattern_start_node

                    # Insert new target base and update links
                    for j in range(tlen):
                        base_target_node: SingleNode = SingleNode(target[j])
                        current_base_target_node.set_next(base_target_node)
                        current_base_target_node = current_base_target_node.get_next()
            
                    # Reconnect original nodes 
                    current_base_target_node.set_next(base_pattern_end_node)
                    
                    # Remove old head with new pattern if it starts at 0
                    if base_pattern_start_index == 0:
                        self.linkedlist.remove_from_front()

                    # Strand length changes by the difference in base length
                    base_target_length_delta = tlen - plen
                    current_strand_length += base_target_length_delta
                    list_new_size = self.linkedlist.get_size() + base_target_length_delta
                    self.linkedlist.set_size(list_new_size)

                    # Search for new pattern matches
                    similar_bases = 0
                    base_pattern_start_index = index + 1
                    base_pattern_start_node = current_base_target_node 
                
                index += 1
                current_base_index += 1
                current_base_node = base_pattern_end_node 

            self.extlist.append(current_strand_length)

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

def test_find_replace():
    my_refgrid = RefGrid()
    # Yes, I am allowed to use .split, sorry :-)
    pattern, target = ("tg", "c") 
    print("Testing cut-and-splice with P = ", pattern, "and T = ", target)
    # Read the refgrid to a linked list
    my_refgrid.read_to_linkedlist("Assignments/a1/test.refgrid")
    # my_refgrid.read_to_linkedlist("Assignments/a1/data/tiny.refgrid")
    # We supply the pattern length for your information
    my_refgrid.cut_and_splice(pattern, len(pattern), target, len(target))
    print(my_refgrid.stringify_spliced_linkedlist(), end="")
    sys.exit(0)

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

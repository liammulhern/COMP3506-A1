"""
COMP3506/7505 S2 2023
The University of Queensland

NOTE: This file will not be used for marking and is here to provide you with
a simple way of testing your data structures. You may edit this file by adding
your own test functionality.
"""

# Import helper libraries
import sys
import argparse
import time
import random

# Import our data structures
from structures.m_extensible_list import ExtensibleList
from structures.m_stack import EStack, LStack
from structures.m_single_linked_list import SingleNode, SingleLinkedList

def test_single_linked_list():
    """
    A simple set of tests for the singly linked list implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Single List Tests ====")

    # Consider expanding these tests into your own methods instead of
    # just doing a bunch of stuff here - this is just to get you started
    
    # OK, let's add some strings to a list
    my_single_list = SingleLinkedList()
    my_single_list.insert_to_front(SingleNode("hello"))
    my_single_list.insert_to_front(SingleNode("world"))
    my_single_list.insert_to_back(SingleNode("algorithms"))

    # Have a look - we can do this due to overriding __str__ in the class
    print(str(my_single_list))

    # Now lets try to find a node
    elem = my_single_list.find_element("world")
    if elem != None:
        print ("Found node with data = ", elem.get_data())

    # And try to delete one
    elem = my_single_list.find_and_remove_element("woo")
    if elem != None:
        print ("Deleted ", elem.get_data())
    else:
        print ("Didn't find element = woo")

    # And try to delete another one
    elem = my_single_list.find_and_remove_element("world")
    if elem != None:
        print ("Deleted ", elem.get_data())
    else:
        print ("Didn't find element = world")

    # Have another look
    print(str(my_single_list))

    # OK, now check size
    print("After 3 insertions and 1 deletion, size = ", my_single_list.get_size())
    assert(my_single_list.get_size() == 2)

def test_extensible_list():
    """
    A simple set of tests for the extensible list implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Extensible List Tests ====")
    my_ex_list = ExtensibleList()

def test_ex_stack():
    """
    A simple set of tests for the extensible list-based stack implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Stack (ExtensibleList) Tests ====")
    my_stack = EStack()

def test_linked_stack():
    """
    A simple set of tests for the linked list-based stack implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Stack (SingleLinkedList) Tests ====")
    my_stack = LStack()


# Benchmark stacks
def benchmark_stacks(n):
    """
    Benchmark the EStack and LStack by pushing and popping n random integers
    and timing the process empirically
    """ 
    es = EStack()
    ls = LStack()

    # Generate a random list of n numbers between 0 and 100
    # I am allowed to use `list` but you are not :-) Sorry!
    randomlist = random.choices(range(0, 100), k=n)

    # Push all, pop all
    t0 = time.time()
    for item in randomlist:
        es.push(item)
    while not es.empty():
        es.pop()
    t1 = time.time()
    total_es = t1-t0
    
    # Push all, pop all
    t0 = time.time()
    for item in randomlist:
        ls.push(item)
    while not es.empty():
        ls.pop()
    t1 = time.time()
    total_ls = t1-t0

    print("ExtensibleArray Stack: ", total_es)
    print("SingleLinkedList Stack: ", total_ls)


# The actual program we're running here
if __name__ == "__main__":

    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description='COMP3506/7505 Assignment One: Data Structure Tests')

    parser.add_argument('--linked-list',  action='store_true', help="Run linked list tests?")
    parser.add_argument('--ex-list',      action='store_true', help="Run extensible list tests?")
    parser.add_argument('--linked-stack', action='store_true', help="Run stack (linked list) tests?")
    parser.add_argument('--ex-stack',     action='store_true', help="Run stack (extensible list) tests?")
    parser.add_argument('--bench-stacks', type=int,            help="Run stacks benchmark with k random integers.")
    parser.set_defaults(stack=False, single_list=False, double_list=False)

    args = parser.parse_args()
    
    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Execute the outcome
    if args.linked_list:
        test_single_linked_list()
    if args.ex_list:
        test_extensible_list()
    if args.linked_stack:
        test_linked_stack()
    if args.ex_stack:
        test_ex_stack()
    if args.bench_stacks is not None:
        benchmark_stacks(args.bench_stacks)

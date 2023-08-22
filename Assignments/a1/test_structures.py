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
    
    test_single_linked_list_init()
    test_single_linked_list_empty_traverse_and_delete()
    test_single_linked_list_insert_to_front()
    test_single_linked_list_insert_to_back()

def test_single_linked_list_init() -> None:
    print("Init:")
    single_list = SingleLinkedList()
    
    print(str(single_list))

    assert(single_list.get_size() == 0)
    assert(single_list.get_head() == None)

def test_single_linked_list_empty_traverse_and_delete() -> None:
    print("Traverse and Delete Empty:")
    single_list = SingleLinkedList()
    
    single_list.traverse_and_delete()
    print(str(single_list))

    assert(single_list.get_size() == 0)
    assert(single_list.get_head() == None)

def test_single_linked_list_insert_to_front() -> None:
    print("Insert to Front:")
    single_list = SingleLinkedList()
    
    node1 = SingleNode("1")
    node2 = SingleNode("2")
    node3 = SingleNode("3")

    single_list.insert_to_front(node1)
    single_list.insert_to_front(node2)
    single_list.insert_to_front(node3)

    print(str(single_list))

    assert(single_list.find_element("3") != None)
    assert(single_list.find_element("2") != None)
    assert(single_list.find_element("1") != None)
    
    assert(single_list.get_size() == 3)
    assert(single_list.get_head() == node3)

def test_single_linked_list_insert_to_back() -> None:
    print("Insert to Back:")
    single_list = SingleLinkedList()
    
    node1 = SingleNode("1")
    node2 = SingleNode("2")
    node3 = SingleNode("3")

    single_list.insert_to_back(node1)
    single_list.insert_to_back(node2)
    single_list.insert_to_back(node3)

    print(str(single_list))

    assert(single_list.find_element("3") != None)
    assert(single_list.find_element("2") != None)
    assert(single_list.find_element("1") != None)
    
    assert(single_list.get_size() == 3)
    assert(single_list.get_head() == node1)

def test_extensible_list():
    """
    A simple set of tests for the extensible list implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Extensible List Tests ====")
    
    test_extensible_list_reset()

    test_extensible_list_str()

    test_extensible_list_get_empty()
    test_extensible_list_get_multiple()

    test_extensible_list_get_at_empty()
    test_extensible_list_get_at_multiple()
    test_extensible_list_get_at_range()

    test_extensible_list_set()
    test_extensible_list_set_multiple()
    test_extensible_list_set_overwrite()

    test_extensible_list_set_at()
    test_extensible_list_set_at_multiple()
    test_extensible_list_set_at_overwrite()
    test_extensible_list_set_at_range()

    test_extensible_list_append_empty()
    test_extensible_list_append_multiple()
    test_extensible_list_append_resize()
    
    test_extensible_list_remove_empty()
    test_extensible_list_remove()
    test_extensible_list_remove_multiple()
    test_extensible_list_remove_contiguous()
    
    test_extensible_list_remove_at_empty()
    test_extensible_list_remove_at()
    test_extensible_list_remove_at_multiple()
    test_extensible_list_remove_at_range()
    test_extensible_list_remove_at_range_bounds()
    test_extensible_list_remove_at_contiguous()

def test_extensible_list_reset() -> None:
    print("Reset: ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")
    ex_list.append("Test1")
    ex_list.append("Test2")
    ex_list.append("Test3")

    assert(ex_list.get_size() == 4)
    assert(ex_list.get_capacity() == 4)

    print(str(ex_list))

    ex_list.reset()

    assert(ex_list.get_size() == 0)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_str() -> None:
    print("Str (Empty): ")
    ex_list = ExtensibleList()

    print(str(ex_list))

    assert(ex_list.get_size() == 0)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_get_empty() -> None:
    print("Get (Empty): ")
    ex_list = ExtensibleList()
    
    print(str(ex_list))

    try:
        data = ex_list[0]
        assert(data != None)
    except Exception as e:
        print(e)

def test_extensible_list_get_multiple() -> None:
    print("Get (Multi): ")
    ex_list = ExtensibleList()
   
    ex_list[0] = "Test0"
    ex_list[1] = "Test1"
    ex_list[2] = "Test2"
    ex_list[3] = "Test3"

    print(str(ex_list))

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")
    assert(ex_list[2] == "Test2")
    assert(ex_list[3] == "Test3")

def test_extensible_list_get_at_empty() -> None:
    print("Get At (Empty Index): ")
    ex_list = ExtensibleList()
    
    print(str(ex_list))

    try:
        data = ex_list.get_at(0)
        assert(data == None)
    except Exception as e:
        print(e)

def test_extensible_list_get_at_multiple() -> None:
    print("Get At (Multi): ")
    ex_list = ExtensibleList()
    
    ex_list.append("Test0")
    ex_list.append("Test1")
    ex_list.append("Test2")
    ex_list.append("Test3")

    print(str(ex_list))

    assert(ex_list.get_at(0) == "Test0")
    assert(ex_list.get_at(1) == "Test1")
    assert(ex_list.get_at(2) == "Test2")
    assert(ex_list.get_at(3) == "Test3")

def test_extensible_list_get_at_range() -> None:
    print("Get At (Range): ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")
    ex_list.append("Test1")
    ex_list.append("Test2")
    ex_list.append("Test3")

    print(str(ex_list))

    assert(ex_list.get_at(4) == None)

def test_extensible_list_set() -> None:
    print("Set: ")
    ex_list = ExtensibleList()
    
    ex_list[0] = "Test0"

    print(str(ex_list))

    assert(ex_list.get_size() == 1)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_set_multiple() -> None:
    print("Set (Multi): ")
    ex_list = ExtensibleList()
    
    ex_list[0] = "Test0"
    ex_list[1] = "Test1"
    ex_list[2] = "Test2"
    ex_list[3] = "Test3"

    print(str(ex_list))

    assert(ex_list.get_size() == 4)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_set_overwrite() -> None:
    print("Set (Overwrite): ")
    ex_list = ExtensibleList()
    
    ex_list[0] = "Test0"
    ex_list[1] = "Test1"
    ex_list[2] = "Test2"

    print(str(ex_list))

    assert(ex_list[0] == "Test0")
    assert(ex_list.get_size() == 3)

    ex_list[0] = "Overwritten"
    
    print(str(ex_list))

    assert(ex_list[0] == "Overwritten")
    assert(ex_list.get_size() == 3)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_set_at() -> None:
    print("Set At: ")
    ex_list = ExtensibleList()
    
    ex_list.set_at(0, "Test1")

    print(str(ex_list))

    assert(ex_list.get_size() == 0)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_set_at_multiple() -> None:
    print("Set At (Multi): ")
    ex_list = ExtensibleList()
    
    ex_list.append("Temp")
    ex_list.append("Temp")
    ex_list.append("Temp")
    ex_list.append("Temp")
    
    print(str(ex_list))
    assert(ex_list.get_size() == 4)
    assert(ex_list.get_capacity() == 4)

    ex_list.set_at(0, "Test0")
    ex_list.set_at(1, "Test1")
    ex_list.set_at(2, "Test2")
    ex_list.set_at(3, "Test3")

    print(str(ex_list))
    assert(ex_list.get_size() == 4)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_set_at_range() -> None:
    print("Set At (Range): ")
    ex_list = ExtensibleList()

    ex_list.append("Temp")
    ex_list.append("Temp")
    
    print(str(ex_list))
    assert(ex_list.get_size() == 2)
    assert(ex_list.get_capacity() == 4)

    ex_list.set_at(0, "Test0")
    ex_list.set_at(1, "Test1")
    ex_list.set_at(3, "Test3")

    print(str(ex_list))

    assert(ex_list.get_size() == 2)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_set_at_overwrite() -> None:
    print("Set At (Overwrite): ")
    ex_list = ExtensibleList()
 
    ex_list.append("Temp")
    ex_list.append("Temp")
    ex_list.append("Temp")
    
    print(str(ex_list))
    assert(ex_list.get_size() == 3)
    assert(ex_list.get_capacity() == 4)

    ex_list.set_at(0, "Test0")
    ex_list.set_at(1, "Test1")
    ex_list.set_at(2, "Test2")

    print(str(ex_list))
    assert(ex_list.get_size() == 3)
    assert(ex_list.get_at(0) == "Test0")

    ex_list.set_at(0, "Overwritten")

    print(str(ex_list))
    assert(ex_list.get_at(0) == "Overwritten")
    assert(ex_list.get_size() == 3)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_append_empty() -> None:
    print("Append (Empty): ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")

    print(str(ex_list))

    assert(ex_list[0] == "Test0")
    assert(ex_list.get_size() == 1)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_append_multiple() -> None:
    print("Append (Multi): ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")
    ex_list.append("Test1")
    ex_list.append("Test2")
    ex_list.append("Test3")

    print(str(ex_list))

    assert(ex_list.get_size() == 4)
    assert(ex_list.get_capacity() == 4)

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")
    assert(ex_list[2] == "Test2")
    assert(ex_list[3] == "Test3")

def test_extensible_list_append_resize() -> None:
    print("Append (Resize): ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")
    ex_list.append("Test1")
    ex_list.append("Test2")
    ex_list.append("Test3")
    ex_list.append("Test4")

    print(str(ex_list))

    assert(ex_list.get_size() == 5)
    assert(ex_list.get_capacity() == 8)

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")
    assert(ex_list[2] == "Test2")
    assert(ex_list[3] == "Test3")
    assert(ex_list[4] == "Test4")

def test_extensible_list_remove_empty() -> None:
    print("Remove (Empty): ")
    ex_list = ExtensibleList()

    print(str(ex_list))

    ex_list.remove("Test0")

    print(str(ex_list))

    assert(ex_list.get_size() == 0)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_remove() -> None:
    print("Remove: ")
    ex_list = ExtensibleList()
    
    ex_list.append("Test0")

    print(str(ex_list))

    ex_list.remove("Test0")

    print(str(ex_list))

    assert(ex_list.get_size() == 0)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_remove_multiple() -> None:
    print("Remove (Multi): ")
    ex_list = ExtensibleList()
    
    ex_list.append("Test0")
    ex_list.append("Test1")

    print(str(ex_list))

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")

    ex_list.remove("Test0")

    assert(ex_list[0] == "Test1")

    print(str(ex_list))

    ex_list.remove("Test1")

    print(str(ex_list))

    assert(ex_list.get_size() == 0)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_remove_contiguous() -> None:
    print("Remove (Contiguous): ")
    ex_list = ExtensibleList()
    
    ex_list.append("Test0")
    ex_list.append("Test1")
    ex_list.append("Test2")

    print(str(ex_list))

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")
    assert(ex_list[2] == "Test2")

    ex_list.remove("Test1")

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test2")

    print(str(ex_list))

    assert(ex_list.get_size() == 2)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_remove_at_empty() -> None:
    print("Remove At (Empty): ")
    ex_list = ExtensibleList()

    print(str(ex_list))

    assert(ex_list.remove_at(0) == None)

    print(str(ex_list))

    assert(ex_list.get_size() == 0)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_remove_at() -> None:
    print("Remove At: ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")

    print(str(ex_list))

    assert(ex_list[0] == "Test0")

    ex_list.remove_at(0)

    print(str(ex_list))

    assert(ex_list.get_size() == 0)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_remove_at_multiple() -> None:
    print("Remove At (Multi): ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")
    ex_list.append("Test1")

    print(str(ex_list))

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")

    ex_list.remove_at(0)

    assert(ex_list[0] == "Test1")

    print(str(ex_list))

    assert(ex_list.get_size() == 1)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_remove_at_range() -> None:
    print("Remove At (Range): ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")
    ex_list.append("Test1")

    print(str(ex_list))

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")

    assert(ex_list.remove_at(3) == None)

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")

    print(str(ex_list))

    assert(ex_list.get_size() == 2)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_remove_at_contiguous() -> None:
    print("Remove At (Contiguous): ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")
    ex_list.append("Test1")
    ex_list.append("Test2")

    print(str(ex_list))

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")
    assert(ex_list[2] == "Test2")

    ex_list.remove_at(1) 

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test2")

    print(str(ex_list))

    assert(ex_list.get_size() == 2)
    assert(ex_list.get_capacity() == 4)

def test_extensible_list_remove_at_range_bounds() -> None:
    print("Remove At (Range Bound): ")
    ex_list = ExtensibleList()

    ex_list.append("Test0")
    ex_list.append("Test1")

    print(str(ex_list))

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")

    assert(ex_list.remove_at(5) == None)

    assert(ex_list[0] == "Test0")
    assert(ex_list[1] == "Test1")

    print(str(ex_list))

    assert(ex_list.get_size() == 2)
    assert(ex_list.get_capacity() == 4)

def test_ex_stack():
    """
    A simple set of tests for the extensible list-based stack implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Stack (ExtensibleList) Tests ====")

    test_ex_stack_push_empty()
    test_ex_stack_push_multiple()

    test_ex_stack_pop_empty()
    test_ex_stack_pop()
    test_ex_stack_pop_multiple_1()
    test_ex_stack_pop_multiple_2()

    test_ex_stack_peek_empty()
    test_ex_stack_peek()
    test_ex_stack_peek_multiple()

def test_ex_stack_push_empty() -> None:
    print("Push (Empty): ")
    ex_stack = EStack()

    print(str(ex_stack))

    ex_stack.push("Test0")

    print(str(ex_stack))

    assert(ex_stack.peek() == "Test0")
    assert(not ex_stack.empty())

def test_ex_stack_push_multiple() -> None:
    print("Push (Multi): ")
    ex_stack = EStack()

    print(str(ex_stack))

    ex_stack.push("Test0")
    ex_stack.push("Test1")
    ex_stack.push("Test2")

    print(str(ex_stack))

    assert(ex_stack.peek() == "Test2")
    assert(not ex_stack.empty())

def test_ex_stack_pop_empty() -> None:
    print("Pop (Empty): ")
    ex_stack = EStack()

    print(str(ex_stack))

    pop = ex_stack.pop()

    print(str(ex_stack))

    assert(pop == None) 
    assert(ex_stack.peek() == None) 
    assert(ex_stack.empty())

def test_ex_stack_pop() -> None:
    print("Pop: ")
    ex_stack = EStack()
    
    ex_stack.push("Test0")

    print(str(ex_stack))

    pop = ex_stack.pop()

    print(str(ex_stack))

    assert(pop == "Test0") 
    assert(ex_stack.peek() == None) 
    assert(ex_stack.empty())

def test_ex_stack_pop_multiple_1() -> None:
    print("Pop (Multi 1): ")
    ex_stack = EStack()
    
    ex_stack.push("Test0")
    ex_stack.push("Test1")
    ex_stack.push("Test2")
    ex_stack.push("Test3")

    print(str(ex_stack))

    pop = ex_stack.pop()

    print(str(ex_stack))

    assert(pop == "Test3") 
    assert(ex_stack.peek() == "Test2") 
    assert(not ex_stack.empty())

def test_ex_stack_pop_multiple_2() -> None:
    print("Pop (Multi 2): ")
    ex_stack = EStack()
    
    ex_stack.push("Test0")
    ex_stack.push("Test1")
    ex_stack.push("Test2")
    ex_stack.push("Test3")

    print(str(ex_stack))

    pop = ex_stack.pop()
    assert(pop == "Test3") 
    assert(ex_stack.peek() == "Test2") 
    assert(not ex_stack.empty())

    print(str(ex_stack))
    pop = ex_stack.pop()
    assert(pop == "Test2") 
    assert(ex_stack.peek() == "Test1") 
    assert(not ex_stack.empty())

    print(str(ex_stack))
    pop = ex_stack.pop()
    assert(pop == "Test1") 
    assert(ex_stack.peek() == "Test0") 
    assert(not ex_stack.empty())

    print(str(ex_stack))
    pop = ex_stack.pop()
    assert(pop == "Test0") 
    assert(ex_stack.peek() == None) 
    assert(ex_stack.empty())

def test_ex_stack_peek() -> None:
    print("Peek: ")
    ex_stack = EStack()
    
    ex_stack.push("Test0")

    print(str(ex_stack))

    assert(ex_stack.peek() == "Test0") 
    assert(not ex_stack.empty())

def test_ex_stack_peek_empty() -> None:
    print("Peek (Empty): ")
    ex_stack = EStack()

    print(str(ex_stack))

    assert(ex_stack.peek() == None) 
    assert(ex_stack.empty())

def test_ex_stack_peek_multiple() -> None:
    print("Peek (Multi): ")
    ex_stack = EStack()

    ex_stack.push("Test0")
    assert(ex_stack.peek() == "Test0") 

    print(str(ex_stack))
    ex_stack.push("Test1")
    assert(ex_stack.peek() == "Test1") 

    print(str(ex_stack))

    assert(not ex_stack.empty())

def test_linked_stack():
    """
    A simple set of tests for the linked list-based stack implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Stack (SingleLinkedList) Tests ====")

    test_l_stack_push_empty()
    test_l_stack_push_multiple()

    test_l_stack_pop_empty()
    test_l_stack_pop()
    test_l_stack_pop_multiple_1()
    test_l_stack_pop_multiple_2()

    test_l_stack_peek_empty()
    test_l_stack_peek()
    test_l_stack_peek_multiple()

def test_l_stack_push_empty() -> None:
    print("Push (Empty): ")
    l_stack = LStack()

    print(str(l_stack))

    l_stack.push("Test0")

    print(str(l_stack))

    assert(l_stack.peek() == "Test0")
    assert(not l_stack.empty())

def test_l_stack_push_multiple() -> None:
    print("Push (Multi): ")
    l_stack = LStack()

    print(str(l_stack))

    l_stack.push("Test0")
    l_stack.push("Test1")
    l_stack.push("Test2")

    print(str(l_stack))

    assert(l_stack.peek() == "Test2")
    assert(not l_stack.empty())

def test_l_stack_pop_empty() -> None:
    print("Pop (Empty): ")
    l_stack = LStack()

    print(str(l_stack))

    pop = l_stack.pop()

    print(str(l_stack))

    assert(pop == None) 
    assert(l_stack.peek() == None) 
    assert(l_stack.empty())

def test_l_stack_pop() -> None:
    print("Pop: ")
    l_stack = LStack()
    
    l_stack.push("Test0")

    print(str(l_stack))

    pop = l_stack.pop()

    print(str(l_stack))

    assert(pop == "Test0") 
    assert(l_stack.peek() == None) 
    assert(l_stack.empty())

def test_l_stack_pop_multiple_1() -> None:
    print("Pop (Multi 1): ")
    l_stack = LStack()
    
    l_stack.push("Test0")
    l_stack.push("Test1")
    l_stack.push("Test2")
    l_stack.push("Test3")

    print(str(l_stack))

    pop = l_stack.pop()

    print(str(l_stack))

    assert(pop == "Test3") 
    assert(l_stack.peek() == "Test2") 
    assert(not l_stack.empty())

def test_l_stack_pop_multiple_2() -> None:
    print("Pop (Multi 2): ")
    l_stack = LStack()
    
    l_stack.push("Test0")
    l_stack.push("Test1")
    l_stack.push("Test2")
    l_stack.push("Test3")

    print(str(l_stack))

    pop = l_stack.pop()
    assert(pop == "Test3") 
    assert(l_stack.peek() == "Test2") 
    assert(not l_stack.empty())

    print(str(l_stack))
    pop = l_stack.pop()
    assert(pop == "Test2") 
    assert(l_stack.peek() == "Test1") 
    assert(not l_stack.empty())

    print(str(l_stack))
    pop = l_stack.pop()
    assert(pop == "Test1") 
    assert(l_stack.peek() == "Test0") 
    assert(not l_stack.empty())

    print(str(l_stack))
    pop = l_stack.pop()
    assert(pop == "Test0") 
    assert(l_stack.peek() == None) 
    assert(l_stack.empty())

def test_l_stack_peek() -> None:
    print("Peek: ")
    l_stack = LStack()
    
    l_stack.push("Test0")

    print(str(l_stack))

    assert(l_stack.peek() == "Test0") 
    assert(not l_stack.empty())

def test_l_stack_peek_empty() -> None:
    print("Peek (Empty): ")
    l_stack = LStack()

    print(str(l_stack))

    assert(l_stack.peek() == None) 
    assert(l_stack.empty())

def test_l_stack_peek_multiple() -> None:
    print("Peek (Multi): ")
    l_stack = LStack()

    l_stack.push("Test0")
    assert(l_stack.peek() == "Test0") 

    print(str(l_stack))
    l_stack.push("Test1")
    assert(l_stack.peek() == "Test1") 

    print(str(l_stack))

    assert(not l_stack.empty())


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

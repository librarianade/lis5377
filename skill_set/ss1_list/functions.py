#!/usr/bin/env python3
"""SkillSet 1 – Lists (functions.py)
Developer: Ayansewa Adedeji
"""


def get_requirements():
    """Function prints program requirements."""
    print("Python Lists")
    print("\nProgram Requirements:")
    print("\tDeveloper: Ayansewa Adedeji")
    print("\t1. Lists (Python data structure): mutable, ordered sequence of elements.")
    print("\t2. Lists are mutable/changeable--that is, can insert, update, delete.")
    print("\t3. Create two lists-- using square brackets [list items]: list = [include list elements here...].")
    print("\t4. Backward-engineer the following program.\n")


def get_list1():
    """Function to create list1."""
    list1 = [1, "test", 3.14, True]
    print("Print list1: ", end="")
    print(list1)
    return list1


def add_list1(test_list):
    """Function to add list elements."""
    print("\nAppend '@' character to end of list1:")
    test_list.append("@")
    print(test_list)


def insert_list1(test_list):
    """Function to insert list elements."""
    print("\nInsert number 6 at beginning of list1:")
    test_list.insert(0, 6)
    print(test_list)


def get_list1_len(test_list):
    """Function to display number of list elements."""
    print("\nDisplay number of list1 elements:")
    print(len(test_list))


def reverse_list1(test_list):
    """Function to reverse list."""
    print("\nReverse list1:")
    test_list.reverse()
    print(test_list)


def remove_last_list1_item(test_list):
    """Function to remove last list element."""
    print("\nRemove last list1 element:")
    test_list.pop()
    print(test_list)


def delete_second_list1_item(test_list):
    """Function to delete element by index."""
    print("\nDelete second element from list1 by *index* (note: index 1=2nd element):")
    del test_list[1]
    print(test_list)


def delete_list1_item_by_value(test_list):
    """Function to delete element by value."""
    print("\nDelete element from list1 by *value* (3.14):")
    test_list.remove(3.14)
    print(test_list)


def delete_all_list1_items(test_list):
    """Function to delete all list elements."""
    print("\nDelete all elements from list1:")
    test_list.clear()
    print(test_list)


def get_list2():
    """Function to create list2."""
    list2 = ["test", "a", "new", "list"]
    print("\nPrint list2: ", end="")
    print(list2)
    return list2


def sort_list2(test_list):
    """Function to sort list alphabetically."""
    print("\nSort elements in list2 alphabetically - using sort():")
    test_list.sort()
    print(test_list)


def reverse_sort_list2(test_list):
    """Function to reverse sort list alphabetically."""
    print("\nSort elements in list2 reverse alphabetically - using sort():")
    test_list.sort(reverse=True)
    print(test_list)

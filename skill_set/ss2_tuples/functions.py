#!/usr/bin/env python3
"""SkillSet 2 - Tuples (functions.py)
Developer: Ayansewa Adedeji
"""


def get_requirements():
    """Function prints program requirements."""
    print("Python Tuples")

    print("\nProgram Requirements:")
    print("\tDeveloper: Ayansewa Adedeji")
    print("\t1. Tuples (Python data structure): immutable (cannot be changed!), ordered sequence of elements.")
    print("\t2. Tuples are immutable/unchangeable--that is, cannot insert, update, delete.")
    print("\t3. Create tuple using parentheses (tuple): tuple = (include elements here...).")
    print("\t4. Reassign tuple with, and w/o parentheses (), aka tuple 'packing'.")
    print("\t5. Use tuple (unpacking), that is, assign values from tuple to sequence of variables.")
    print("\t6. Backward-engineer the following program.\n")


def get_tuple():
    """Function to create tuple."""
    my_tuple = (1, "test", 3.14, True)

    print("Print my_tuple: ", end="")
    print(my_tuple)

    return my_tuple


def unpack_tuple(test_tuple):
    """Function to unpack tuple."""
    elem1, elem2, elem3, elem4 = test_tuple

    print("\nPrint my_tuple unpacking:")
    print(f"elem1={elem1}, elem2={elem2}, elem3={elem3}, elem4={elem4}")


def get_tuple_len(test_tuple):
    """Function to display number of tuple elements."""
    print("\nDisplay number of my_tuple elements:")
    print(len(test_tuple))


def print_third_item(test_tuple):
    """Function to print third tuple element."""
    print("\nPrint third element in my_tuple:")
    print(test_tuple[2])


def print_slice(test_tuple):
    """Function to print tuple slice."""
    print("\nPrint \"slice\" of my_tuple (second and third elements):")
    print(test_tuple[1:3])


def reassign_tuple_parentheses():
    """Function to reassign tuple using parentheses."""
    my_tuple = (1, 2, 3, 4)

    print("\nReassign my_tuple using parentheses.")
    print("Print reassigned my_tuple:")
    print(my_tuple)

    return my_tuple


def reassign_tuple_packing():
    """Function to reassign tuple using packing."""
    my_tuple = 5, 6, 7, 8

    print("\nReassign my_tuple using \"packing\" method (no parentheses).")
    print("Print reassigned my_tuple:")
    print(my_tuple)

    return my_tuple


def delete_tuple_note():
    """Function prints note about deleting tuple."""
    print("\nDelete my_tuple:")
    print("Note: will generate error, if trying to print after delete, as it no longer exists.")

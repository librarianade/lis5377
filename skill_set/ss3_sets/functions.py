#!/usr/bin/env python3
"""SkillSet 3 - Sets (functions.py)
Developer: Ayansewa Adedeji
"""


def get_requirements():
    """Function prints program requirements."""
    print("Python Sets - like mathematical sets!")

    print("\nProgram Requirements:")
    print("\tDeveloper: Ayansewa Adedeji")
    print("\t1. Sets: mutable, heterogeneous, unordered sequence of elements, CANNOT contain duplicate values.")
    print("\t2. Sets are mutable/changeable--that is, can insert, update, delete.")
    print("\t3. Sets cannot contain other mutable items like list, set, or dictionary.")
    print("\t4. Sets are unordered, CANNOT use indexing (or slicing) to access, update, delete elements.")
    print("\t5. Two methods to create sets:")
    print("\t\ta. Create set using curly brackets {set}")
    print("\t\tb. Create set using set() function")
    print("\t6. Backward-engineer the following program.\n")


def get_set1():
    """Create set1 using curly brackets."""
    print("Print set1 created using curly brackets:")
    print("Note: Following values used: 2, 'test', 3.14, True")
    print("Note: Value sequence *used* not guaranteed!")

    set1 = {2, "test", 3.14, True}
    print(set1)

    return set1


def print_set_type(s):
    """Print set type."""
    print("\nPrint set type:")
    print(type(s))


def get_set2():
    """Create set2 using set() with list."""
    print("\nPrint set2 created using set() function with list:")

    set2 = set([2, "test", 3.14, True])
    print(set2)

    return set2


def get_set3():
    """Create set3 using set() with tuple."""
    print("\nPrint set3 created using set() function with tuple:")

    set3 = set((2, "test", 3.14, True))
    print(set3)

    return set3


def get_set_len(s):
    """Display number of set elements."""
    print("\nDisplay number of set elements:")
    print(len(s))


def add_item(s):
    """Add set element."""
    print("\nAdd set element (5) using add() method:")
    s.add(5)
    print(s)


def update_items(s):
    """Update set with multiple values."""
    print("\nDisplay updated set elements:")
    print("Note: Updated with following values: 1, 2, 3, 4")
    s.update([1, 2, 3, 4])
    print(s)


def discard_item(s):
    """Discard element."""
    print("\nDiscard 4:")
    s.discard(4)
    print(s)


def remove_item(s):
    """Remove element."""
    print("\nRemove 'test':")
    s.remove("test")
    print(s)


def print_min(s):
    """Display minimum value."""
    print("\nDisplay minimum value:")
    print(min(s))


def print_max(s):
    """Display maximum value."""
    print("\nDisplay maximum value:")
    print(max(s))


def print_sorted(s):
    """Display sorted set elements."""
    print("\nDisplay set elements:")
    print(sorted(s))


def print_sum(s):
    """Display sum of numeric values."""
    print("\nDisplay sum of values:")
    print(sum([x for x in s if isinstance(x, (int, float, bool))]))


def delete_all(s):
    """Delete all set elements."""
    print("\nDelete all set elements:")
    s.clear()
    print(s)

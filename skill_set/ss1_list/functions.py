"""
SkillSet 1 – Lists Functions
Developer: Ayansewa Adedeji
"""

def append_at(lst):
    # Append '@' to end of list
    lst.append('@')


def insert_at_beginning(lst):
    # Insert number 6 at beginning of list
    lst.insert(0, 6)


def reverse_list(lst):
    # Reverse list
    lst.reverse()


def remove_last_element(lst):
    # Remove last list element
    lst.pop()


def delete_second_element_by_index(lst):
    # Delete second element (index 1)
    del lst[1]


def delete_element_by_value(lst, value):
    # Delete first matching element by value
    lst.remove(value)


def delete_all_elements(lst):
    # Delete all elements from list
    lst.clear()


def sort_list_alpha(lst):
    # Sort alphabetically
    lst.sort()


def sort_list_reverse_alpha(lst):
    # Sort reverse alphabetically
    lst.sort(reverse=True)

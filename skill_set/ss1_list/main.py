"""
SkillSet 1 – Lists
Developer: Ayansewa Adedeji
"""

from functions import *

# Create list1
list1 = [1, 'test', 3.14, True]

print("Print list1:", list1)

append_at(list1)
print("\nAppend '@' character to end of list1:")
print(list1)

insert_at_beginning(list1)
print("\nInsert number 6 at beginning of list1:")
print(list1)

print("\nDisplay number of list1 elements:")
print(len(list1))

reverse_list(list1)
print("\nReverse list1:")
print(list1)

remove_last_element(list1)
print("\nRemove last list1 element:")
print(list1)

delete_second_element_by_index(list1)
print("\nDelete second element from list1 by index (note: index 1=2nd element):")
print(list1)

delete_element_by_value(list1, 3.14)
print("\nDelete element from list1 by value (3.14):")
print(list1)

delete_all_elements(list1)
print("\nDelete all elements from list1:")
print(list1)

# Create list2
list2 = ['test', 'a', 'new', 'list']
print("\nPrint list2:", list2)

sort_list_alpha(list2)
print("\nSort elements in list2 alphabetically - using sort():")
print(list2)

sort_list_reverse_alpha(list2)
print("\nSort elements in list2 reverse alphabetically - using sort():")
print(list2)

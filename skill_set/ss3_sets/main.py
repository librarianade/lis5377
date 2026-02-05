"""
SkillSet 3 – Sets
Developer: Ayansewa Adedeji
"""

from functions import *

# Create sets
set1 = {True, 2, 3.14, 'test'}
set2 = set([2, 'test', 3.14, True])
set3 = set((2, 'test', 3.14, True))

print("Print set1 created using curly brackets:")
display_set(set1)

print("\nPrint set1 type:")
display_type(set1)

print("\nPrint set2 created using set() function with list:")
display_set(set2)

print("\nPrint set2 type:")
display_type(set2)

print("\nPrint set3 created using set() function with tuple:")
display_set(set3)

print("\nPrint set3 type:")
display_type(set3)

print("\nDisplay number of set1 elements:")
display_length(set1)

add_element(set1, 5)
print("\nAdd set element (5) using add() method:")
display_set(set1)

print("\nDisplay number of set1 elements:")
display_length(set1)

update_set(set1)
print("\nDisplay updated set1 elements:")
display_set(set1)

print("\nDisplay number of set1 elements:")
display_length(set1)

discard_element(set1, 4)
print("\nDiscard 4:")
display_set(set1)

print("\nLength of set1:")
display_length(set1)

remove_element(set1, 'test')
print("\nRemove 'test':")
display_set(set1)

print("\nLength of set1:")
display_length(set1)

print("\nDisplay minimum value:")
display_min(set1)

print("\nDisplay maximum value:")
display_max(set1)

print("\nDisplay set1 elements:")
display_set(set1)

print("\nDisplay sum of values:")
display_sum(set1)

clear_set(set1)
print("\nDelete all set elements:")
display_set(set1)

print("\nLength of set1:")
display_length(set1)

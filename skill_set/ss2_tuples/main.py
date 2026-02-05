"""
SkillSet 2 – Tuples
Developer: Ayansewa Adedeji
"""

from functions import *

my_tuple = (1, 'test', 3.14, True)

print("Print my_tuple:")
display_tuple(my_tuple)

print("\nPrint my_tuple unpacking:")
unpack_tuple(my_tuple)

print("\nDisplay number of my_tuple elements:")
display_length(my_tuple)

print("\nPrint third element in my_tuple:")
display_third_element(my_tuple)

print("\nPrint slice of my_tuple (second and third elements):")
display_slice(my_tuple)

# Reassign tuple using parentheses
my_tuple = (1, 2, 3, 4)

print("\nPrint reassigned my_tuple:")
display_tuple(my_tuple)

# Reassign tuple using packing (no parentheses)
my_tuple = 5, 6, 7, 8

print("\nPrint reassigned my_tuple:")
display_tuple(my_tuple)

# Delete tuple
del my_tuple

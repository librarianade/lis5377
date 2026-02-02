from functions import *

def main():
    print("Python Tuples")
    print("Program Requirements:")
    print("Developer: Ayansewa Adedeji\n")

    my_tuple = build_tuple()
    print(f"Print my_tuple: {my_tuple}\n")

    e1, e2, e3, e4 = unpack_tuple(my_tuple)
    print("Print my_tuple unpacking:")
    print(f"elem1={e1}, elem2={e2}, elem3={e3}, elem4={e4}\n")

    print("Display number of my_tuple elements:")
    print(tuple_length(my_tuple))
    print()

    print("Print third element in my_tuple:")
    print(third_element(my_tuple))
    print()

    print('Print "slice" of my_tuple (second and third elements):')
    print(slice_second_third(my_tuple))
    print()

    print("Reassign my_tuple using parentheses.")
    my_tuple = reassign_tuple_parentheses()
    print("Print reassigned my_tuple:")
    print(my_tuple)
    print()

    print('Reassign my_tuple using "packing" method (no parentheses).')
    my_tuple = reassign_tuple_packing()
    print("Print reassigned my_tuple:")
    print(my_tuple)
    print()

    # The screenshot mentions delete and that printing after delete would error.
    # We can demonstrate deletion without printing afterward.
    del my_tuple
    print("Delete my_tuple:")
    print("Note: will generate error, if trying to print after delete, as it no longer exists.")

if __name__ == "__main__":
    main()

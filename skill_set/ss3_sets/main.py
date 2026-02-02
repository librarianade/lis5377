from functions import *

def main():
    print("Python Sets - like mathematical sets!")
    print("Program Requirements:")
    print("Developer: Ayansewa Adedeji\n")

    set1 = create_set1()
    print("Print set1 created using curly brackets:")
    print("Note: following values used: 2, 'test', 3.14, True")
    print("Note: Value sequence *used* not guaranteed!")
    print(set1, "\n")

    print("Print set1 type:")
    print(set_type(set1), "\n")

    set2 = create_set2_from_list()
    print("Print set2 created using set() function with list:")
    print(set2, "\n")

    print("Print set2 type:")
    print(set_type(set2), "\n")

    set3 = create_set3_from_tuple()
    print("Print set3 created using set() function with tuple:")
    print(set3, "\n")

    print("Print set3 type:")
    print(set_type(set3), "\n")

    print("Display number of set1 elements:")
    print(set_len(set1), "\n")

    print("Add set element (5) using add() method:")
    print(add_value(set1, 5), "\n")

    print("Display number of set1 elements:")
    print(set_len(set1), "\n")

    print("Display updated set1 elements:")
    print("Note: Updated with following values: 1, 2, 3, 4")
    print("Note: Sets can ONLY contain unique elements! (Note: True=1, and value 2 already exist!)")
    print(update_set(set1, [1, 2, 3, 4]), "\n")

    print("Display number of set1 elements:")
    print(set_len(set1), "\n")

    print("Discard 4:")
    print(discard_value(set1, 4), "\n")

    print("Length of set1:")
    print(set_len(set1), "\n")

    print("Remove 'test':")
    print(remove_value(set1, "test"), "\n")

    print("Length of set1:")
    print(set_len(set1), "\n")

    print("Note: When deleting set element that doesn't exist, discard() ignores it, but remove() raises KeyError!\n")

    print("Display minimum value (Note: True=1):")
    print(min_value(set1), "\n")

    print("Display maximum value:")
    print(max_value(set1), "\n")

    print("Display set1 elements:")
    print(set1, "\n")

    print("Display sum of values (*must* be numeric, or able to convert to numeric):")
    print(sum_values(set1), "\n")

    print("Delete all set elements:")
    print(clear_set(set1), "\n")

    print("Length of set1:")
    print(set_len(set1))

if __name__ == "__main__":
    main()

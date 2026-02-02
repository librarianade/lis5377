from functions import *

def main():
    print("Python Lists")
    print("Program Requirements:")
    print("Developer: Ayansewa Adedeji\n")

    list1 = build_list1()
    print(f"Print list1: {list1}\n")

    print("Append '@' character to end of list1:")
    print(append_at(list1.copy()) if False else append_at(list1))  # keeps exact list1 flow
    print()

    print("Insert number 6 at beginning of list1:")
    print(insert_six_front(list1))
    print()

    print("Display number of list1 elements:")
    print(count_elements(list1))
    print()

    print("Reverse list1:")
    print(reverse_list(list1))
    print()

    print("Remove last list1 element:")
    print(remove_last(list1))
    print()

    print("Delete second element from list1 by *index* (note: index 1=2nd element):")
    print(delete_second_by_index(list1))
    print()

    print("Delete element from list1 by *value* (3.14):")
    print(delete_by_value(list1, 3.14))
    print()

    print("Delete all elements from list1:")
    print(clear_list(list1))
    print()

    list2 = build_list2()
    print(f"Print list2: {list2}\n")

    print("Sort elements in list2 alphabetically - using sort():")
    print(sort_list_alpha(list2))
    print()

    print("Sort elements in list2 reverse alphabetically - using sort():")
    print(sort_list_reverse_alpha(list2))
    print()

if __name__ == "__main__":
    main()

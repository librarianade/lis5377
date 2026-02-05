#!/usr/bin/env python3
"""SkillSet 1 Lists (main.py)
Developer: Ayansewa Adedeji
"""

import functions as f


def main():
    """Function docstring goes here..."""
    f.get_requirements()

    your_list = f.get_list1()
    f.add_list1(your_list)
    f.insert_list1(your_list)
    f.get_list1_len(your_list)
    f.reverse_list1(your_list)
    f.remove_last_list1_item(your_list)
    f.delete_second_list1_item(your_list)
    f.delete_list1_item_by_value(your_list)
    f.delete_all_list1_items(your_list)

    new_list = f.get_list2()
    f.sort_list2(new_list)
    f.reverse_sort_list2(new_list)


if __name__ == "__main__":
    main()

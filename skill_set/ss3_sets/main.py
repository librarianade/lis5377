#!/usr/bin/env python3
"""SkillSet 3 Sets (main.py)
Developer: Ayansewa Adedeji
"""

import functions as f


def main():
    """Function docstring goes here..."""
    f.get_requirements()

    set1 = f.get_set1()
    f.print_set_type(set1)

    set2 = f.get_set2()
    f.print_set_type(set2)

    set3 = f.get_set3()
    f.print_set_type(set3)

    f.get_set_len(set1)
    f.add_item(set1)
    f.get_set_len(set1)

    f.update_items(set1)
    f.get_set_len(set1)

    f.discard_item(set1)
    f.get_set_len(set1)

    f.remove_item(set1)
    f.get_set_len(set1)

    f.print_min(set1)
    f.print_max(set1)
    f.print_sorted(set1)
    f.print_sum(set1)

    f.delete_all(set1)
    f.get_set_len(set1)


if __name__ == "__main__":
    main()

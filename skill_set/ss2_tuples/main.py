#!/usr/bin/env python3
"""SkillSet 2 – Tuples (main.py)
Developer: Ayansewa Adedeji
"""

import functions as f


def main():
    """Function docstring goes here..."""
    f.get_requirements()

    my_tuple = f.get_tuple()
    f.unpack_tuple(my_tuple)
    f.get_tuple_len(my_tuple)
    f.print_third_item(my_tuple)
    f.print_slice(my_tuple)

    my_tuple = f.reassign_tuple_parentheses()
    my_tuple = f.reassign_tuple_packing()

    f.delete_tuple_note()


if __name__ == "__main__":
    main()

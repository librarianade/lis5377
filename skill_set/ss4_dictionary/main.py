#!/usr/bin/env python3
"""module docstring goes here"""

import functions as f


def main():
    """program entry"""
    f.get_requirements()

    my_dictionary = f.build_dictionary()
    f.print_dictionary(my_dictionary)

    f.print_items_builtin(my_dictionary)
    f.print_items_loop(my_dictionary)

    f.display_keys(my_dictionary)
    f.display_values(my_dictionary)

    f.print_value_by_key(my_dictionary, "Alaska")
    f.count_items(my_dictionary)

    f.add_element(my_dictionary, "Arizona", "Scottsdale")
    f.update_element(my_dictionary, "Arizona", "Phoenix")

    f.delete_element(my_dictionary, "Arizona")
    f.delete_all(my_dictionary)


if __name__ == "__main__":
    main()

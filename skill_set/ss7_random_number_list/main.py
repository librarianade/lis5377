#!/usr/bin/env python3

import functions as f


def main():
    """Program entry. Calling environment to user-defined functions."""
    # initialize variable(s)
    size = 0
    your_list = []  # create empty list

    # function calls
    f.get_requirements()
    size = f.get_list_size()
    # use below for unit testing
    # print(size)
    # exit()
    your_list = f.create_list(size)
    # print(your_list)  # check pseudo-random number list
    f.sort_list(your_list)


if __name__ == "__main__":
    main()
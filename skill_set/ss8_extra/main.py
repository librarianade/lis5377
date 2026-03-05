#!/usr/bin/env python3
"""compound interest menu program"""

import functions as f


def main():
    f.get_requirements()

    while True:
        command = f.menu()

        if command == "e":
            print("\nThank you for using our compound interest program.")
            break

        f.run_calculation(command)


if __name__ == "__main__":
    main()
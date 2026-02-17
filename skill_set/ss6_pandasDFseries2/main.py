#!/usr/bin/env python3
"""module docstring goes here"""

import functions as f


def main():
    """program entry"""
    f.get_requirements()
    f.print_pandas_version()

    f.display_data()
    f.display_type()

    f.total_passengers()
    f.total_perished()
    f.total_males_perished()
    f.percent_males_of_total_perished()

    f.count_age_condition()
    f.unique_home_countries()
    f.unique_home_countries_excluding_england_france()


if __name__ == "__main__":
    main()

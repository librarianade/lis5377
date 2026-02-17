"""function library for pandas DataFrames/Series"""

import pandas as pd

# read data into pandas "global" DataFrame (for access in functions below)
df = pd.read_csv("titanic.csv")


def get_requirements():
    """print program requirements"""
    print("Pandas DataFrames and Series Data Structures\n")
    print("Program Requirements:")
    print("Developer: Ayansewa Adedeji")
    print("1. Working with pandas DataFrames and Series data structures, for tabular data handling.")
    print("2. DataFrame: Two-dimensional labeled data structure (i.e., rows/cols).")
    print("3. DataFrame: Series collection. Each column is Series sharing same index.")
    print("4. Using multiple conditions: not, and, or.")
    print("5. Logical operators, numeric comparisons, counting/comparing NaN/non-NaN values.\n")
    print("Note: not, and, or statements require truth-values.")
    print('Pandas requires "bitwise" (overloaded operators): not (~), and (&), or (|).\n')


def print_pandas_version():
    """print pandas version"""
    print("Print pandas version:")
    print(pd.__version__)
    print("")


def display_data():
    """display data"""
    print("Display data:")
    print(df)
    print("")


def display_type():
    """display data type"""
    print("Display type:")
    print(type(df))
    print("")


def total_passengers():
    """total number of passengers"""
    print("Total number of passengers:", len(df))
    print("")


def total_perished():
    """total number perished"""
    # assumes survived column values like "yes"/"no"
    perished = (df["survived"].astype(str).str.lower() == "no").sum()
    print("Total number perished:", perished)
    print("")


def total_males_perished():
    """total males perished"""
    males_perished = (
        (df["gender"].astype(str).str.lower() == "male")
        & (df["survived"].astype(str).str.lower() == "no")
    ).sum()
    print("Total males perished:", males_perished)
    print("")


def percent_males_of_total_perished():
    """percentage of males who died from total perished"""
    perished = (df["survived"].astype(str).str.lower() == "no").sum()
    males_perished = (
        (df["gender"].astype(str).str.lower() == "male")
        & (df["survived"].astype(str).str.lower() == "no")
    ).sum()

    pct = (males_perished / perished) * 100
    print("Percentage of males who died from total perished:", f"{pct:.2f}%")
    print("")


def count_age_condition():
    """count passengers older than 70 OR younger than 5"""
    # age may have NaN; coerce safely
    age = pd.to_numeric(df["age"], errors="coerce")
    count_val = ((age > 70) | (age < 5)).sum()
    print("Total number of passengers older than 70 OR younger than 5:", int(count_val))
    print("")


def unique_home_countries():
    """unique home countries"""
    countries = df["country"].dropna()
    print("Total number of unique home countries:", countries.nunique())
    print("")


def unique_home_countries_excluding_england_france():
    """unique home countries excluding England or France"""
    countries = df["country"].dropna().astype(str)
    filtered = countries[~countries.str.lower().isin(["england", "france"])]
    print("Total number of unique home countries, not including England or France:", filtered.nunique())
    print("")

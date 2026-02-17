"""function library for Python dictionaries"""

def get_requirements():
    """function prints program requirements"""
    print("\nPython Dictionaries")
    print("\nProgram Requirements:\n"
          "Developer: Ayansewa Adedeji\n"
          "1. Dictionaries (Python data structure): unordered key:value pairs.\n"
          "2. Dictionary: an associative array (also known as hashes).\n"
          "3. Any key in dictionary is associated (or mapped) to a value (i.e., any Python data type).\n"
          "4. Keys: must be of immutable type (string, number, or tuple with immutable elements) and must be unique.\n"
          "5. Values: can be any data type and can repeat.\n"
          "6. Dictionaries have key:value pairs instead of single values; differentiating a dictionary from a set.\n"
          "7. Two methods to create dictionaries:\n"
          "   a. Initialize dictionary with key/value pairs.\n"
          "   b. Create empty dictionary, using curly braces {}: my_dictionary = {}\n"
          "      Then, assign values to keys: my_dictionary['key1'] = \"some value\"\n"
          "8. Backward-engineer the following program.\n")


def build_dictionary():
    """create and return starter dictionary"""
    my_dictionary = {
        "Alaska": "Juneau",
        "Texas": "Austin",
        "California": "Sacramento",
        "Montana": "Helena",
        "New Mexico": "Santa Fe"
    }
    return my_dictionary


def print_dictionary(my_dictionary):
    """print dictionary and its type"""
    print("\nPrint dictionary:")
    print(my_dictionary)

    print("\nPrint data structure type:")
    print(type(my_dictionary))


def print_items_builtin(my_dictionary):
    """print dictionary items using built-in function"""
    print("\nReturn dictionary's (key, value) pairs, built-in function:")
    print(my_dictionary.items())


def print_items_loop(my_dictionary):
    """print dictionary items using loop"""
    print("\nOr, use looping structure to return dictionary's (key, value) pairs, built-in function:")
    for k, v in my_dictionary.items():
        print(f"key:{k}, value:{v}")


def display_keys(my_dictionary):
    """display all keys"""
    print("\nDisplay all keys, built-in function:")
    print(my_dictionary.keys())


def display_values(my_dictionary):
    """display all values"""
    print("\nDisplay all values in dictionary, built-in function:")
    print(my_dictionary.values())


def print_value_by_key(my_dictionary, key):
    """print value by key"""
    print("\nPrint value using key:")
    print(my_dictionary[key])


def count_items(my_dictionary):
    """count items"""
    print("\nCount number of items (key:value pairs) in dictionary:")
    print(len(my_dictionary))


def add_element(my_dictionary, key, value):
    """add element"""
    my_dictionary[key] = value
    print("\nPrint dictionary after added element:")
    print(my_dictionary)


def update_element(my_dictionary, key, value):
    """update element"""
    my_dictionary[key] = value
    print("\nPrint dictionary after updated element:")
    print(my_dictionary)


def delete_element(my_dictionary, key):
    """delete element"""
    print(f"\nDelete '{key}' element:")
    del my_dictionary[key]

    print("\nPrint dictionary after deleted element:")
    print(my_dictionary)


def delete_all(my_dictionary):
    """delete all elements"""
    print("\nDelete all dictionary elements:")
    my_dictionary.clear()
    print(my_dictionary)

    print(type(my_dictionary))

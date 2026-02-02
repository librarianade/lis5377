def build_tuple():
    return (1, "test", 3.14, True)

def unpack_tuple(t):
    elem1, elem2, elem3, elem4 = t
    return elem1, elem2, elem3, elem4

def tuple_length(t):
    return len(t)

def third_element(t):
    return t[2]

def slice_second_third(t):
    return t[1:3]

def reassign_tuple_parentheses():
    return (1, 2, 3, 4)

def reassign_tuple_packing():
    return 5, 6, 7, 8

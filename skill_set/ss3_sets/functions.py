def create_set1():
    return {2, "test", 3.14, True}

def set_type(s):
    return type(s)

def create_set2_from_list():
    return set([2, "test", 3.14, True])

def create_set3_from_tuple():
    return set((2, "test", 3.14, True))

def set_len(s):
    return len(s)

def add_value(s, value):
    s.add(value)
    return s

def update_set(s, iterable):
    s.update(iterable)
    return s

def discard_value(s, value):
    s.discard(value)
    return s

def remove_value(s, value):
    s.remove(value)
    return s

def min_value(s):
    return min(s)

def max_value(s):
    return max(s)

def sum_values(s):
    return sum(s)

def clear_set(s):
    s.clear()
    return s

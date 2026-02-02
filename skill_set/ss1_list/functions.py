def build_list1():
    return [1, "test", 3.14, True]

def append_at(lst):
    lst.append("@")
    return lst

def insert_six_front(lst):
    lst.insert(0, 6)
    return lst

def count_elements(lst):
    return len(lst)

def reverse_list(lst):
    lst.reverse()
    return lst

def remove_last(lst):
    lst.pop()
    return lst

def delete_second_by_index(lst):
    del lst[1]
    return lst

def delete_by_value(lst, value):
    lst.remove(value)
    return lst

def clear_list(lst):
    lst.clear()
    return lst

def build_list2():
    return ["test", "a", "new", "list"]

def sort_list_alpha(lst):
    lst.sort()
    return lst

def sort_list_reverse_alpha(lst):
    lst.sort(reverse=True)
    return lst

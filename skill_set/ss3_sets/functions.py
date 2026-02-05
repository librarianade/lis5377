"""
SkillSet 3 – Sets Functions
Developer: Ayansewa Adedeji
"""

def display_set(st):
    print(st)

def display_type(st):
    print(type(st))

def display_length(st):
    print(len(st))

def add_element(st, value):
    st.add(value)

def update_set(st):
    st.update([1, 2, 3, 4])

def discard_element(st, value):
    st.discard(value)

def remove_element(st, value):
    st.remove(value)

def display_min(st):
    print(min(st))

def display_max(st):
    print(max(st))

def display_sum(st):
    # only numeric values allowed
    numeric_values = [x for x in st if isinstance(x, (int, float))]
    print(sum(numeric_values))

def clear_set(st):
    st.clear()

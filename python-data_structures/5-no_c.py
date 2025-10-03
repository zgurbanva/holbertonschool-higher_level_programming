#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string"""
    new_str = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_str += ch
    return new_str

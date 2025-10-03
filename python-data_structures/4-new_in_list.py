#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list without modifying the original list"""
    if my_list is None:
        return None

    # make a copy of the list
    new_list = my_list[:]

    # check boundaries
    if idx < 0 or idx >= len(my_list):
        return new_list

    # replace in the copy
    new_list[idx] = element
    return new_list

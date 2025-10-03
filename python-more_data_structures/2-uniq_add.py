#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once per integer)"""
    return sum(set(my_list))

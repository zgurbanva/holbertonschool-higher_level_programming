#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    if my_list is not None:
        for i in reversed(my_list):
            print("{:d}".format(i))

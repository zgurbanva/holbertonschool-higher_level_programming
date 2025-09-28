#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list
and adds a method to print the list in a sorted order.
"""


class MyList(list):
    """
    MyList extends the built-in list class with an extra method.
    """

    def print_sorted(self):
        """
        Print the list, but sorted in ascending order.

        The original list remains unchanged.
        """
        print(sorted(self))

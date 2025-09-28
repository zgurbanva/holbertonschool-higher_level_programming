#!/usr/bin/python3
"""
This module provides the lookup function.
It returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods are to be listed.

    Returns:
        list: A list of strings containing attributes and methods.
    """
    return dir(obj)

#!/usr/bin/python3
"""Defines class MyList that inherits from list."""


class MyList(list):
    """Custom list class with extra behavior."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original."""
        print(sorted(self))

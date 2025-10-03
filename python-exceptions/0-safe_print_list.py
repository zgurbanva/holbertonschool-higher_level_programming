#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list safely"""
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count

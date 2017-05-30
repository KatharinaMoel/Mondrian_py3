"""
public functions
"""

# !/usr/bin/env python
# coding=utf-8

try:
    cmp
except NameError:
    def cmp(x, y):
        if x < y:
            return -1
        elif x > y:
           return 1
        else:
            return 0

def cmp_str(element1, element2):
    """
    compare number in str format correctly
    """
    try:
        return cmp(int(element1), int(element2))
    except ValueError:
        return cmp(element1, element2)

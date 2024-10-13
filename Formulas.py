# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:51:28 2024

@author: fossn
"""


def F_to_C (f):
    """Converts Fahrenheit to Celsius."""
    return round((f - 32)* 5 / 9)
    
def C_to_F (c):
    """Converts Celsius to Farenheit."""
    return round((c * 9 / 5) + 32)

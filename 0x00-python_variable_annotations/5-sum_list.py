#!/usr/bin/env python3
"""
Module that provides a function to sum a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floats and return the result.
    
    Args:
        input_list (List[float]): List of float numbers
    
    Returns:
        float: The sum of all floats in the list
    """
    return sum(input_list)

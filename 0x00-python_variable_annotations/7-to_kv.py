#!/usr/bin/env python3
"""
Module that provides a function to create a tuple with string and squared number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.
    
    Args:
        k (str): The string value
        v (Union[int, float]): The number to be squared
    
    Returns:
        Tuple[str, float]: Tuple containing the string and squared number as float
    """
    return (k, v * v)

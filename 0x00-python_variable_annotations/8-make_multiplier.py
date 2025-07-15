#!/usr/bin/env python3
"""
Module that provides a function to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.
    
    Args:
        multiplier (float): The multiplier value
    
    Returns:
        Callable[[float], float]: Function that multiplies a float by multiplier
    """
    def multiply(x: float) -> float:
        """
        Multiply a float by the multiplier.
        
        Args:
            x (float): The float to multiply
        
        Returns:
            float: The result of multiplication
        """
        return x * multiplier
    
    return multiply

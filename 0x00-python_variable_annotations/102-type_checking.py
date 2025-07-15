#!/usr/bin/env python3
"""
Module that provides a function to zoom an array.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom an array by repeating each element factor times.
    
    Args:
        lst (Tuple): The tuple to zoom
        factor (int): The zoom factor
    
    Returns:
        List: The zoomed array as a list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

#!/usr/bin/env python3
"""
Module that provides a function to get element lengths from an iterable.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with each element and its length.
    
    Args:
        lst (Iterable[Sequence]): An iterable of sequences
    
    Returns:
        List[Tuple[Sequence, int]]: List of tuples containing each element and its length
    """
    return [(i, len(i)) for i in lst]

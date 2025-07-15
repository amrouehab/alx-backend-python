#!/usr/bin/env python3
"""
Module that provides a function to safely get the first element of a sequence.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence if it exists, otherwise None.
    
    Args:
        lst (Sequence[Any]): A sequence of any type
    
    Returns:
        Union[Any, None]: The first element or None if sequence is empty
    """
    if lst:
        return lst[0]
    else:
        return None

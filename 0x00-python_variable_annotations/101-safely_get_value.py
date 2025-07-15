#!/usr/bin/env python3
"""
Module that provides a function to safely get a value from a mapping.
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a mapping with a default fallback.
    
    Args:
        dct (Mapping): The mapping to get value from
        key (Any): The key to look for
        default (Union[T, None]): Default value if key not found
    
    Returns:
        Union[Any, T]: The value from mapping or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default

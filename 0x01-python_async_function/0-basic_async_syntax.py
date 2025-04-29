#!/usr/bin/env python3
"""Module that contains an asynchronous coroutine to wait for a random delay."""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously wait for a random delay between 0 and max_delay seconds.
    
    Args:
        max_delay (int): Maximum number of seconds to wait. Default is 10.
    
    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


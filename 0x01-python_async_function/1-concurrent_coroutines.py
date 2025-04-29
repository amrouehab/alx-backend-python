#!/usr/bin/env python3
"""Module that spawns multiple wait_random coroutines concurrently."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously run wait_random n times and return the list of delays.
    
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random call.
    
    Returns:
        List[float]: List of all delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays


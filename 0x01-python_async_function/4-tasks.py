#!/usr/bin/env python3
"""Module to run multiple task_wait_random coroutines concurrently."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously run task_wait_random n times and return list of delays.
    
    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for each call.
    
    Returns:
        List[float]: List of all delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays


#!/usr/bin/env python3
"""Module to measure the runtime of an asynchronous function."""

import time
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of wait_n and return average time per task.
    
    Args:
        n (int): Number of times wait_random is spawned.
        max_delay (int): Maximum delay for each call.
    
    Returns:
        float: Total execution time divided by n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n


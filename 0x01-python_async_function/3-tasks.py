#!/usr/bin/env python3
"""Module that creates an asyncio.Task for wait_random."""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio.Task that waits for a random delay.
    
    Args:
        max_delay (int): Maximum delay.
    
    Returns:
        asyncio.Task: The created task.
    """
    return asyncio.create_task(wait_random(max_delay))


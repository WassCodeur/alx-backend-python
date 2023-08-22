#!/usr/bin/env python3
"""execute multiple"""
import asyncio
from typing import List
wait_ran = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return List
    n: (int)
    max_delay: (int)
    return: (List)
    """
    tasks = [wait_ran(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

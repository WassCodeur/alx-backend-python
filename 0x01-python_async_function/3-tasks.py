#!/usr/bin/env python3
"""tasks"""
from asyncio import create_task, Task
wait_ran = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """return task
    max_delay (int)
    return task
    """
    task = create_task(wait_ran(max_delay))
    return task

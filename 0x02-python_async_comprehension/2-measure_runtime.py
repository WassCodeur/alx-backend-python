#!/usr/bin/env python3
"""run time for four"""
import asyncio
import time
async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measure four async_comp run time
    none
    return: run_time(int)
    """
    start_at = time.time()
    result = [async_comp() for _ in range(4)]
    await asyncio.gather(*result)
    end_at = time.time()
    run_time = end_at - start_at
    return run_time

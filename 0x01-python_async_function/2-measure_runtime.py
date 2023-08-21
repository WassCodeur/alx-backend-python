#!/usr/bin/env python3
"""measure the runtime"""
import asyncio
import time
waitn = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the runtime
    n (int)
    max_delay (in)
    return (float)
    """
    start_at = time.time()
    asyncio.run(waitn(n, max_delay))
    end_at = time.time()
    duration = end_at - start_at
    return (duration / n)

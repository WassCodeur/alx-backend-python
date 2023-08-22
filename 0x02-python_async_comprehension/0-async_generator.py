#!/usr/bin/env python3
""" Async Gnerator"""
import asyncio
import random


async def async_generator():
    """asynchronous generator
    none
    yield random number between 0 to 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

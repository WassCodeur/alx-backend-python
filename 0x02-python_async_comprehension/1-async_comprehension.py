#!/usr/bin/env python3
"""Async comprehension"""
import asyncio
async_gene = __import__('0-async_generator').async_generator


async def async_comprehension():
    """async comprehension
    none
    return list
    """
    result = [num async for num in (async_gene())]
    return result

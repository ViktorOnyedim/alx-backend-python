#!/usr/bin/env python3
"""Asynchronous coroutine"""


import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Asynchronously spawn wait_random n times with the specified max_delay
    """
    delays: List[float] = []

    tasks = [wait_random(max_delay) for i in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

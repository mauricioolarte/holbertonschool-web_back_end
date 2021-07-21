#!/usr/bin/env python3
''' asynchronous coroutine that takes in an integer argument (max_delay) '''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' asynchronous coroutine that takes in an integer argument '''
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time

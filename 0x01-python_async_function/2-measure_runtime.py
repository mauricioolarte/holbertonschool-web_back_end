#!/usr/bin/env python3
'''
    takes in 2 int arguments (in this order): n
    and max_delay. You will spawn wait_random n
    times with the specified max_delay
'''

import asyncio
import random
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    ''' calculte time excution '''
    s = time.time()
    list = await wait_n(n, max_delay)
    total_time = time.time() - s
    if n == 0:
        return total_time
    return total_time / n

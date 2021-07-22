#!/usr/bin/env python3
'''
    takes in 2 int arguments (in this order): n
    and max_delay. You will spawn wait_random n
    times with the specified max_delay
'''

import asyncio
import random
import time
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Callable[[float], float]:
    ''' import a asyncio task '''
    task = asyncio.ensure_future(wait_random(max_delay))
    return task

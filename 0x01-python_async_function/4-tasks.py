#!/usr/bin/env python3
'''
    takes in 2 int arguments (in this order): n
    and max_delay. You will spawn wait_random n
    times with the specified max_delay
'''


import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' n: number of call '''
    answ = []
    for value in range(n):
        flag = 0
        val = await task_wait_random(max_delay)
        if len(answ) == 0:
            answ.append(val)
            continue
        for element in range(len(answ)):
            if val < answ[element]:
                answ.insert(element, val)
                flag = 1
                break
        if flag == 0:
            answ.append(val)
    # answ.sort()
    return answ

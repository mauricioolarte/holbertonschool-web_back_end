#!/usr/bin/env python3

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[int, None, None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random()

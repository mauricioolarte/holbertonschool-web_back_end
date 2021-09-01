#!/usr/bin/env python3
""" redis project to learn """

from functools import wraps
import redis
from typing import Union, Optional, Callable
from uuid import uuid4, UUID


def count_calls(method: Callable) -> Callable:
    """ decorator that takes a single method Callable argument and returns
    a Callable """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ conserve the original function’s name """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """  decorator to store the history of inputs and outputs """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ conserve the original function’s name """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(fn: Callable):
    """ function to display the history of calls of a particular function."""
    redisf = redis.Redis()
    f_name = fn.__qualname__
    n_calls = redisf.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')

    ins = redisf.lrange(f_name + ":inputs", 0, -1)
    outs = redisf.lrange(f_name + ":outputs", 0, -1)

    for input, output in zip(ins, outs):
        try:
            inputs = input.decode('utf-8')
        except Exception:
            inputs = ""
        try:
            outputs = output.decode('utf-8')
        except Exception:
            ooutputs = ""

        print(f'{f_name}(*{inputs}) -> {outputs}')


class Cache:
    """ tore an instance of the Redis client """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """  method should generate a random key"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """  convert the data back to the desired format."""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """  automatically parametrize  """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """  automatically parametrize  """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value

#!/usr/bin/env python3
"""  """

from functools import wraps
import redis
import requests
from typing import Callable

redis = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ count times a request has been made """
    @wraps(method)
    def wrapper(url):
        """ conserve the original function’s name """
        redis.incr(f"count:{url}")
        rchtml = redis.get(f"cached:{url}")
        if rchtml:
            return rchtml.decode('utf-8')

        ghtml = method(url)
        redis.setex(f"cached:{url}", 10, ghtml)
        return ghtml
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Uses the requests module to obtain the HTML
    content of a particular URL and returns it.
    """
    req = requests.get(url)
    return req.text

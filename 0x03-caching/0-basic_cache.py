#!/usr/bin/python3

""" Create a class BasicCache that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """dictionary from the parent class BaseCaching"""

    def put(self, key, item):
        """Puts item in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets item from cache"""
        return self.cache_data.get(key, None)

#!/usr/bin/python3
""" Create a class LIFOCache that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ class LIFOCache that inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.cacheList = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.cacheList:
                last = self.cacheList.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.cacheList:
            self.cacheList.append(key)
        else:
            self.lastItemlist(key)

    def get(self, key):
        """ Gets item from cache """
        return self.cache_data.get(key, None)

    def lastItemlist(self, item):
        """ Moves element to last idx of list """
        length = len(self.cacheList)
        if self.cacheList[length - 1] != item:
            self.cacheList.remove(item)
            self.cacheList.append(item)

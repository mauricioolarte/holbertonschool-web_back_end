#!/usr/bin/python3
""" Create a class FIFOCache that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache that inherits from BaseCaching and is a FIFO caching system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.cacheList = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        if key not in self.cacheList:
            self.cacheList.append(key)
        else:
            self.lastItemlist(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.firstItemList(self.cacheList)
            if first:
                self.cacheList.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Gets item from cache """
        return self.cache_data.get(key, None)

    def lastItemlist(self, item):
        """ Move element to end of list """
        length = len(self.cacheList)
        if self.cacheList[length - 1] != item:
            self.cacheList.remove(item)
            self.cacheList.append(item)

    @staticmethod
    def firstItemList(array):
        """ Get first element"""
        return array[0] if array else None

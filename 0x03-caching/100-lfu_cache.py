#!/usr/bin/python3
""" class LFUCache that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """class LFUCache that inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ superconstructor """
        super().__init__()
        self.cacheList = []
        self.counter = {}

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        cuantity = self.counter.get(key, None)

        if cuantity is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.firstItemList(self.cacheList)
            if first:
                self.cacheList.pop(0)
                del self.cache_data[first]
                del self.counter[first]
                print("DISCARD: {}".format(first))

        if key not in self.cacheList:
            self.cacheList.insert(0, key)
        self.moveStartlist(key)

    def get(self, key):
        """ Gets item from cache """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.counter[key] += 1
            self.moveStartlist(key)
        return item

    def moveStartlist(self, item):
        """  """
        length = len(self.cacheList)

        position = self.cacheList.index(item)
        cuantity = self.counter[item]

        for i in range(position, length):
            if i != (length - 1):
                next = self.cacheList[i + 1]
                rest = self.counter[next]

                if rest > cuantity:
                    break

        self.cacheList.insert(i + 1, item)
        self.cacheList.remove(item)

    @staticmethod
    def firstItemList(array):
        """ Get first element of list"""
        return array[0] if array else None
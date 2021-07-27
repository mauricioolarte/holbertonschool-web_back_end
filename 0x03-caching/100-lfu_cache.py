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

        item_count = self.counter.get(key, None)

        if item_count is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.cacheList)
            if first:
                self.cacheList.pop(0)
                del self.cache_data[first]
                del self.counter[first]
                print("DISCARD: {}".format(first))

        if key not in self.cacheList:
            self.cacheList.insert(0, key)
        self.toRight(key)

    def get(self, key):
        """ Gets item from cache """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.counter[key] += 1
            self.toRight(key)
        return item

    def toRight(self, item):
        """ Moves element  """
        length = len(self.cacheList)

        index = self.cacheList.index(item)
        item_count = self.counter[item]

        for i in range(index, length):
            if i != (length - 1):
                next = self.cacheList[i + 1]
                next_count = self.counter[next]

                if next_count > item_count:
                    break

        self.cacheList.insert(i + 1, item)
        self.cacheList.remove(item)

    @staticmethod
    def get_first_list(array):
        """ Get first element """
        return array[0] if array else None
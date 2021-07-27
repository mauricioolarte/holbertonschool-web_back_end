#!/usr/bin/python3
""" class LFUCache that inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ class LFUCache that inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ superconstructor """
        super().__init__()
        self.cacheList = []
        self.elements = {}

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.elements.get(key, None)

        if item_count is not None:
            self.elements[key] += 1
        else:
            self.elements[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.firstElementlist(self.cacheList)
            if first:
                self.cacheList.pop(0)
                del self.cache_data[first]
                del self.elements[first]
                print("DISCARD: {}".format(first))

        if key not in self.cacheList:
            self.cacheList.insert(0, key)
        self.mv_right_list(key)

    def get(self, key):
        """ Gets item from cache """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.elements[key] += 1
            self.mv_right_list(key)
        return item

    def mv_right_list(self, item):
        """ Moves element to the right, taking into account LFU """
        length = len(self.cacheList)

        position = self.cacheList.index(item)
        item_count = self.elements[item]

        for i in range(position, length):
            if i != (length - 1):
                next = self.cacheList[i + 1]
                next_count = self.elements[next]

                if next_count > item_count:
                    break

        self.cacheList.insert(i + 1, item)
        self.cacheList.remove(item)

    @staticmethod
    def firstElementlist(array):
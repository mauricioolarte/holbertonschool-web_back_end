#!/usr/bin/python3
""" Create a class LRUCache that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ class LRUCache that inherits from BaseCaching and is a caching system LRU caching """

    def __init__(self):
        """ superconstructor """
        super().__init__()
        self.itemList = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.firstItemList(self.itemList)
            if first:
                self.itemList.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

        if key not in self.itemList:
            self.itemList.append(key)
        else:
            self.lastItemlist(key)

    def get(self, key):
        """ Gets item from cache """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.lastItemlist(key)
        return item

    def lastItemlist(self, item):
        """ Moves element to end of list """
        length = len(self.itemList)
        if self.itemList[length - 1] != item:
            self.itemList.remove(item)
            self.itemList.append(item)

    @staticmethod
    def firstItemList(array):
        """ Get first element of list """
        return array[0] if array else None

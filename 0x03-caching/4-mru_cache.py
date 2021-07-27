#!/usr/bin/python3
""" class MRUCache that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ class MRUCache that inherits from BaseCaching and is a caching MRU system"""

    def __init__(self):
        """ superconstructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.queue:
                last = self.queue.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.lastItemlist(key)

    def get(self, key):
        """ Gets item from list """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.lastItemlist(key)
        return item

    def lastItemlist(self, item):
        """ Moves element to end of list """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

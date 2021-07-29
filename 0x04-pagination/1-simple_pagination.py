#!/usr/bin/env python3
'''
named index_range that takes two integer arguments page and page_size
'''


from typing import List
import math
import csv


def index_range(page, page_size):
    '''  takes two integer arguments page and page_size
        return a tuple of size two containing a start index and an end
        index corresponding '''
    return ((page - 1)*page_size, (page*page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        resp = []
        assert isinstance(page, int) is True and isinstance(
            page_size, int) is True, "values must be int"
        assert page > 0 and page_size > 0, "Value must be positive"
        ranges = index_range(page, page_size)
        values = self.dataset()
        max_ranges = len(values)
        min_limit = ranges[0]
        max_range = ranges[1]
        if ranges[0] > max_ranges:
            return []

        for value in range(min_limit, max_range):
            if value < max_ranges:
                resp.append(values[value])
        return resp

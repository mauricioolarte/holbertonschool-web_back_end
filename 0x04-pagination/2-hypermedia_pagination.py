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
        '''get data from file'''
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        ''' get dictionary '''
        data = self.get_page(page, page_size)

        data_set = self.__dataset
        len_set = len(data_set) if data_set else 0

        total_pages = ceil(len_set / page_size) if data_set else 0

        if not data:
            page_size = 0
        else:
            page_size = len(data)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        resp = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return resp

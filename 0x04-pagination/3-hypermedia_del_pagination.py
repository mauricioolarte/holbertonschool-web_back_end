#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ get index """

        values = self.indexed_dataset()

        assert isinstance(index, int) and index < (len(values) - 1)

        counter = 0
        counter2 = index
        data = []
        while (counter < page_size and index < len(values)):
            value = values.get(counter2, None)
            if value:
                data.append(value)
                counter += 1
            counter2 += 1

        next_index = None
        while (counter2 < len(values)):
            value = values.get(counter2, None)
            if value:
                next_index = counter2
                break
            counter2 += 1

        resp = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }

        return resp

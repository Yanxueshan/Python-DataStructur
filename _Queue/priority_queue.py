'''
    数据结构--03--优先级队列（基于最大堆MaxHeap实现）
'''
from _Queue.queue_base import QueueBase
from MaxHeap.max_heap import MaxHeap

__author__ = 'Yan'
__date__ = '2019/3/18 14:41'


class PriorityQueue(QueueBase):
    '''
        数据结构--03--优先级队列（基于最大堆MaxHeap实现）
    '''
    def __init__(self):
        self._data = MaxHeap()

    def get_size(self):
        return self._data.get_size()

    def is_empty(self):
        return self._data.is_empty()

    def enqueue(self, value):
        self._data.add(value)

    def dequeue(self):
        return self._data.extract_max()

    def get_front(self):
        return self._data.find_max()

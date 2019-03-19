'''
    数据结构--03--队列（基于数组Array实现）
'''
from Array.array import Array
from _Queue.queue_base import QueueBase

__author__ = 'Yan'
__date__ = '2018/11/19 20:26'


class ArrayQueue(QueueBase):
    '''
        数据结构--03--队列（基于数组Array实现）
    '''
    def __init__(self, capacity=10):
        self._array = Array(capacity=capacity)

    def get_size(self):
        '''
            获取队列中元素个数
        '''
        return self._array.get_size()

    def is_empty(self):
        '''
            判断队列是否为空
        '''
        return self._array.is_empty()

    def enqueue(self, value):
        '''
            入队，往队列中插入值为value的元素
        '''
        self._array.add_last(value)

    def dequeue(self):
        '''
            出队，从队列中删除队首元素，并返回队首元素的值
        '''
        return self._array.remove_first()

    def get_front(self):
        '''
            获取队首的元素值
        '''
        return self._array.get_first()

    def get_capacity(self):
        '''
            返回队列的空间容量
        '''
        return self._array.get_capacity()


def array_queue_test():
    '''
        测试队列代码是否正确
    '''
    queue = ArrayQueue()
    for i in range(10):
        queue.enqueue(i)
    print(queue.get_size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.get_front())


if __name__ == "__main__":
    array_queue_test()

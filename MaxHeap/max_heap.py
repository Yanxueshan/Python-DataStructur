'''
    数据结构--08--最大堆（基于数组Array实现）
    本次讨论的最大堆是一个二叉堆，具有以下几个特点：
        1. 二叉堆是一个完全二叉树（把元素顺序排列成树的形状）
        2. 其父节点的值总是大于等于子节点的值
        3. 以i节点为例，其父节点为(i - 1) / 2，左子节点为 (2 * i + 1)，右子节点为(2 * i + 2)
    拓展：
        1. D叉堆
        2. 索引堆
        3. 斐波那契堆
        4. 二项堆
'''
from random import randint
from Array.array import Array

__author__ = 'Yan'
__date__ = '2018/3/17 23:11'


class MaxHeap:
    '''
        数据结构--08--最大堆（基于数组Array实现）
    '''
    def __init__(self, array=None, capacity=None):
        if isinstance(array, Array):
            self._data = array
            for i in range(self._parent(array.get_size() - 1), -1, -1):
                self._sift_down(i)
            return
        if capacity is None:
            self._data = Array()
        else:
            self._data = Array(capacity=capacity)

    def get_size(self):
        '''
            返回最大堆MaxHeap中元素个数
        '''
        return self._data.get_size()

    def is_empty(self):
        '''
            判断最大堆MaxHeap是否为空
        '''
        return self._data.is_empty()

    def add(self, value):
        '''
            向最大堆MaxHeap中添加值为value的元素，共分为两步：
                1. 将元素添加在数组Array的末尾
                2. 对末尾元素进行Sift UP操作
        '''
        self._data.add_last(value)
        self._sift_up(self.get_size() - 1)

    def _sift_up(self, index):
        '''
            Sift UP 上浮，若子节点的值大于父节点的值，则Sift UP
        '''
        while index > 0 and self._data.get(index) > self._data.get(self._parent(index)):
            self._data.swap(index, self._parent(index))
            index = self._parent(index)

    def _sift_down(self, index):
        '''
            Sift Down下沉，若父节点小于子节点的值，则Sift Down
        '''
        while self._left_child(index) < self.get_size():
            left_child_index = self._left_child(index)
            right_child_index = self._right_child(index)

            # 获取左子节点和右子节点中最大值所在的索引，为max_index
            max_index = left_child_index
            if right_child_index < self.get_size() and self._data.get(left_child_index) < self._data.get(right_child_index):
                max_index = right_child_index

            # 如果当前index的值大于左右子节点中的最大值，那么直接break
            if self._data.get(index) > self._data.get(max_index):
                break

            self._data.swap(index, max_index)
            index = max_index

    def find_max(self):
        '''
            找到最大堆MaxHeap中的最大元素
        '''
        if self.is_empty():
            raise ValueError("can not find max, MaxHeap is Empty")
        return self._data.get_first()

    def extract_max(self):
        '''
            取出最大堆MaxHeap中的最大元素，总共分两步：
                1. 将第一个元素（最大值）于最后一个元素交换
                2. 对交换后的第一个元素进行Sfit Down操作
        '''
        ret = self.find_max()
        self._data.swap(0, self.get_size()-1)
        self._data.remove_last()
        self._sift_down(0)
        return ret

    def replace(self, value):
        '''
            取出最大堆MaxHeap中的最大元素，并放入一个新的元素（替换掉最大元素）
        '''
        ret = self.find_max()
        self._data.set(0, value)
        self._sift_down(0)
        return ret

    def _parent(self, index):
        '''
            返回索引为index的父亲节点所在的索引
        '''
        if index == 0:
            raise ValueError("index 0 has no parent")
        return (index - 1) // 2

    def _left_child(self, index):
        '''
            返回索引为index的左子节点所在的索引
        '''
        return 2 * index + 1

    def _right_child(self, index):
        '''
            返回索引为index的右子节点所在的索引
        '''
        return 2 * index + 2


def max_heap_test(max_heap):
    '''
        测试MaxHeap代码书写是否正确
    '''
    for i in range(10):
        max_heap.add(randint(1, 100000))

    for data in max_heap._data:
        print(data, end='  ')

    print('\n' + '-------result--------')
    for i in range(max_heap.get_size()):
        print(max_heap.extract_max())
    print('-------end-----------')


def max_heap_test2():
    '''
        测试MaxHeap代码书写是否正确
    '''
    array = Array()
    for i in range(10):
        array.add_last(randint(1, 100000))

    max_heap = MaxHeap(array)

    for data in max_heap._data:
        print(data, end='  ')

    print('\n' + '-------result--------')
    for i in range(max_heap.get_size()):
        print(max_heap.extract_max())
    print('-------end-----------')


if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap_test(max_heap)
    max_heap_test2()

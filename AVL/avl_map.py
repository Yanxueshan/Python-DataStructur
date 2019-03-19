'''
    数据结构--07--Map（基于AVL树进行实现）
'''
from Map.map_base import MapBase
from AVL.avl_tree import AVLTree

__author__ = 'Yan'
__date__ = '2019/3/19 19:53'


class AVLMap(MapBase):
    '''
        数据结构--07--Map（基于AVL树进行实现）
    '''
    def __init__(self):
        self._avl = AVLTree()

    def __getitem__(self, key):
        return self._avl.getter(key)

    def __setitem__(self, key, value):
        self._avl.setter(key, value)

    def add(self, key, value):
        self._avl.add(key, value)

    def remove(self, key):
        return self._avl.remove(key)

    def getter(self, key):
        return self._avl.getter(key)

    def setter(self, key, value):
        self._avl.setter(key, value)

    def contains(self, key):
        return self._avl.contains(key)

    def get_size(self):
        return self._avl.get_size()

    def is_empty(self):
        return self._avl.is_empty()

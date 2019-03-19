'''
    数据结构--06--Set（基于AVL树进行实现）
'''
from Set.set_base import SetBase
from AVL.avl_tree import AVLTree

__author__ = 'Yan'
__date__ = '2019/3/19 19:47'


class AVLSet(SetBase):
    '''
        数据结构--06--Set（基于AVL树进行实现）
    '''
    def __init__(self):
        self._avl = AVLTree()

    def add(self, value):
        self._avl.add(value, None)

    def remove(self, value):
        return self._avl.remove(value)

    def contains(self, value):
        return self._avl.contains(value)

    def get_size(self):
        return self._avl.get_size()

    def is_empty(self):
        return self._avl.is_empty()

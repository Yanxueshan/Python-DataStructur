'''
    数据结构--06--集合Set（基于二分搜索树BST实现）
'''
import time
from Set.set_base import SetBase
from Binary_Search_Tree.BST import BST

__author__ = 'Yan'
__date__ = '2018/3/17 15:42'


class BSTSet(SetBase):
    '''
        数据结构--06--集合Set（基于二分搜索树BST实现）
    '''
    def __init__(self):
        self.bst = BST()

    def get_size(self):
        return self.bst.get_size()

    def is_empty(self):
        return self.bst.is_empty()

    def add(self, value):
        self.bst.add(value)

    def remove(self, value):
        self.bst.remove(value)

    def contains(self, value):
        return self.bst.contains(value)


def bst_set_test(bst_set):
    '''
        测试BSTSet是否书写正确
    '''
    with open('shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    start_time = time.time()
    for word in words:
        bst_set.add(word)
    print('total words: ', len(words))
    print("unique words: ", bst_set.get_size())
    print("contains word 'This': ", bst_set.contains('This'))
    print('total time: {} seconds'.format(time.time() - start_time))


if __name__ == '__main__':
    bst_set = BSTSet()
    bst_set_test(bst_set)

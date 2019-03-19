'''
    数据结构--11--UnionFind（并查集）
'''
import abc

__author__ = 'Yan'
__date__ = '2019/3/18 16:47'


class UnionFindBase(metaclass=abc.ABCMeta):
    '''
        数据结构--11--UnionFind（并查集）
    '''
    @abc.abstractmethod
    def is_connected(self, p, q):
        '''
            判断元素p和q是否相连
        '''
        pass

    def union_elements(self, p, q):
        '''
            将两个元素p和q相连接
        '''
        pass

    def get_size(self):
        '''
            返回UnionFind中的元素个数
        '''
        pass

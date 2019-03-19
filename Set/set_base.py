'''
    数据结构--06--集合Set需要实现的方法
'''
import abc

__author__ = 'Yan'
__date__ = '2018/3/17 15:42'


class SetBase(metaclass=abc.ABCMeta):
    '''
        继承SetBase需要实现的方法，即集合Set需要实现的方法
    '''
    @abc.abstractmethod
    def add(self, value):
        '''
            向集合Set中添加元素value
        '''
        pass

    @abc.abstractmethod
    def remove(self, value):
        '''
            从集合Set中删除元素value
        '''
        pass

    @abc.abstractmethod
    def contains(self, value):
        '''
            查询集合Set中是否包含value，包含返回True，否则返回False
        '''
        pass

    @abc.abstractmethod
    def get_size(self):
        '''
            返回集合Set中元素的个数
        '''
        pass

    @abc.abstractmethod
    def is_empty(self):
        '''
            判断集合Set是否为空
        '''
        pass

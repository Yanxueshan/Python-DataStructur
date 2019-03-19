'''
    数据结构--07--映射Map需要实现的方法
'''
import abc

__author__ = 'Yan'
__date__ = '2018/3/17 15:48'


class MapBase(metaclass=abc.ABCMeta):
    '''
        继承MapBase需要实现的方法，即映射Map需要实现的方法
    '''
    @abc.abstractmethod
    def add(self, key, value):
        '''
            向映射Map中添加键值对key: value
        '''
        pass

    @abc.abstractmethod
    def remove(self, key):
        '''
            从映射Map中删除元素key
        '''
        pass

    @abc.abstractmethod
    def getter(self, key):
        '''
            获取映射Map中key对应的value
        '''
        pass

    @abc.abstractmethod
    def setter(self, key, value):
        '''
            将映射Map中key的值修改为value，如果key不存在，则添加一个新节点
        '''
        pass

    @abc.abstractmethod
    def contains(self, key):
        '''
            查询映射Map中是否包含key，包含返回True，否则返回False
        '''
        pass

    @abc.abstractmethod
    def get_size(self):
        '''
            返回映射Map中元素的个数
        '''
        pass

    @abc.abstractmethod
    def is_empty(self):
        '''
            判断映射Map是否为空
        '''
        pass

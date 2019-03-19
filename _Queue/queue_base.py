'''
    数据结构--03--队列需要实现的方法（利用metaclass）
'''
import abc

__author__ = 'Yan'
__date__ = '2018/11/19 22:39'


class QueueBase(metaclass=abc.ABCMeta):
    '''
        继承QueueBase需要实现的方法，即队列所需实现的方法
    '''

    @abc.abstractmethod
    def get_size(self):
        '''
            获取队列中元素个数
        '''
        pass

    @abc.abstractmethod
    def is_empty(self):
        '''
            判断队列是否为空
        '''
        pass

    @abc.abstractmethod
    def enqueue(self, value):
        '''
            入队，往队列中插入值为value的元素
        '''
        pass

    @abc.abstractmethod
    def dequeue(self):
        '''
            出队，从队列中删除队首元素
        '''
        pass

    @abc.abstractmethod
    def get_front(self):
        '''
            获取队首的元素值
        '''
        pass

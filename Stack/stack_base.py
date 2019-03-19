'''
    数据结构--04--栈需要实现的方法（利用metaclass）
'''
import abc

__author__ = 'Yan'
__date__ = '2018/11/19 22:41'


class StackBase(metaclass=abc.ABCMeta):
    '''
        继承StackBase需要实现的方法，即栈所需实现的方法
    '''

    @abc.abstractmethod
    def get_size(self):
        '''
            获取栈中元素个数
        '''
        pass

    @abc.abstractmethod
    def is_empty(self):
        '''
            判断栈是否为空
        '''
        pass

    @abc.abstractmethod
    def push(self, value):
        '''
            入栈，往栈中插入值为value的元素
        '''
        pass

    @abc.abstractmethod
    def pop(self):
        '''
            出栈，从栈中删除栈顶元素
        '''
        pass

    @abc.abstractmethod
    def top(self):
        '''
            返回栈顶元素的值
        '''
        pass

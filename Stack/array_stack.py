'''
    数据结构--04--栈（基于队列Array实现）
'''
from Array.array import Array
from Stack.stack_base import StackBase

__author__ = 'Yan'
__date__ = '2018/11/19 20:01'


class ArrayStack(StackBase):
    '''
        数据结构--03--栈（基于队列Array实现）
    '''
    def __init__(self, capacity=10):
        self.array = Array(capacity=capacity)

    def get_size(self):
        '''
            获取栈中元素个数
        '''
        return self.array.get_size()

    def is_empty(self):
        '''
            判断栈是否为空
        '''
        return self.array.is_empty()

    def push(self, value):
        '''
            入栈，往栈中插入值为value的元素
        '''
        self.array.add_last(value)

    def pop(self):
        '''
            出栈，从栈中删除栈顶元素
        '''
        return self.array.remove_last()

    def top(self):
        '''
            返回栈顶元素的值
        '''
        return self.array.get_last()

    def get_capacity(self):
        '''
            获取栈的空间容量
        '''
        return self.array.get_capacity()


def array_stack_test():
    '''
        测试栈代码是否正确
    '''
    stack = ArrayStack()
    print(stack.is_empty())
    for i in range(10):
        stack.push(i)

    print(stack.get_size())
    print(stack.get_capacity())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.top())
    print(stack.get_size())


if __name__ == "__main__":
    array_stack_test()

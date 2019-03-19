'''
    数据结构--04--栈（基于LinkedList实现）
'''
from Linked_List.linked_list import LinkedList
from Stack.stack_base import StackBase

__author__ = 'Yan'
__date__ = '2018/11/19 22:49'


class LinkedListStack(StackBase):
    '''
        数据结构--03--栈（基于LinkedList实现）
    '''
    def __init__(self):
        self._linked_list = LinkedList()

    def get_size(self):
        return self._linked_list.size

    def is_empty(self):
        return self._linked_list.is_empty()

    def push(self, value):
        self._linked_list.add_last(value)

    def pop(self):
        return self._linked_list.remove_last()

    def top(self):
        return self._linked_list.get_last()


def linked_list_stack_test():
    stack = LinkedListStack()
    print(stack.is_empty())
    for i in range(10):
        stack.push(i)

    print(stack.get_size())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.top())
    print(stack.get_size())


if __name__ == "__main__":
    linked_list_stack_test()

'''
    数据结构--03--队列（基于链表LinkedList实现）
'''
from Linked_List.linked_list import LinkedList
from _Queue.queue_base import QueueBase

__author__ = 'Yan'
__date__ = '2018/11/19 22:39'


class LinkedListQueue(QueueBase):
    '''
        数据结构--03--队列（基于链表LinkedList实现）
    '''
    def __init__(self):
        self._linked_list = LinkedList()

    def get_size(self):
        return self._linked_list.size

    def is_empty(self):
        return self._linked_list.is_empty()

    def enqueue(self, value):
        self._linked_list.add_last(value)

    def dequeue(self):
        return self._linked_list.remove_first()

    def get_front(self):
        return self._linked_list.get_first()


def linked_list_queue_test():
    '''
        测试队列代码是否正确
    '''
    queue = LinkedListQueue()
    for i in range(10):
        queue.enqueue(i)
    print(queue.get_size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.get_front())


if __name__ == "__main__":
    linked_list_queue_test()

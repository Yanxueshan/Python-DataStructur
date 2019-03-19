'''
    数据结构--06--集合Set（基于链表LinkedList实现）
'''
import time
from Set.set_base import SetBase
from Linked_List.linked_list import LinkedList

__author__ = 'Yan'
__date__ = '2018/3/17 15:42'


class LinkedListSet(SetBase):
    '''
        数据结构--06--集合Set（基于链表LinkedList实现）
    '''
    def __init__(self):
        self._list = LinkedList()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()

    def contains(self, value):
        return self._list.contains(value)

    def add(self, value):
        if self.contains(value):
            return
        self._list.add_first(value)

    def remove(self, value):
        self._list.remove_element(value)


def linked_list_set_test(linked_list_set):
    '''
        测试LinkedListSet是否书写正确
    '''
    with open('shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    start_time = time.time()
    for word in words:
        linked_list_set.add(word)
    print('total words: ', len(words))
    print("unique words: ", linked_list_set.get_size())
    print("contains word 'This': ", linked_list_set.contains('This'))
    print('total time: {} seconds'.format(time.time() - start_time))


if __name__ == '__main__':
    linked_list_set = LinkedListSet()
    linked_list_set_test(linked_list_set)

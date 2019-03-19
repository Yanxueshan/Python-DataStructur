'''
    数据结构--07--映射Map（基于链表LinkedList实现）
'''
import time
from Map.map_base import MapBase

__author__ = 'Yan'
__date__ = '2018/3/17 15:48'


class LinkedListMap(MapBase):
    '''
        数据结构--07--映射Map（基于链表LinkedList实现）
    '''
    class _Node:
        def __init__(self, key=None, value=None, node_next=None):
            self.key = key
            self.value = value
            self.node_next = node_next

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, key, value):
        cur = self._dummy_head
        for i in range(self._size):
            cur = cur.node_next

        add_node = self._Node(key, value)
        cur.node_next = add_node
        self._size += 1

    def find_node(self, key):
        '''
            在映射Map中找到key对应的节点node
        '''
        cur = self._dummy_head.node_next
        for i in range(self._size):
            if cur.key == key:
                node = cur
                break
            else:
                cur = cur.node_next
        else:
            raise IndexError("{} is not exist".format(key))

        return node

    def remove(self, key):
        pre = self._dummy_head
        for i in range(self._size):
            cur = pre.node_next
            if cur.key == key:
                pre.node_next = cur.node_next
                result = cur.value
                cur.node_next = None
                self._size -= 1
                break
            else:
                pre = pre.node_next
        else:
            raise IndexError("{} is not exist".format(key))

        return result

    def getter(self, key):
        node = self.find_node(key)
        return node.value

    def setter(self, key, value):
        try:
            node = self.find_node(key)
            node.value = value
        except IndexError:
            self.add(key, value)

    def contains(self, key):
        try:
            self.find_node(key)
            return True
        except IndexError:
            return False


def linked_list_map_test(linked_list_map):
    '''
        测试LinkedListMap代码书写是否有误
    '''
    with open('shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    start_time = time.time()
    for word in words:
        if linked_list_map.contains(word):
            linked_list_map.setter(word, linked_list_map.getter(word)+1)
        else:
            linked_list_map.add(word, 1)

    print('total words: ', len(words))
    print("unique words: ", linked_list_map.get_size())
    print("contains word 'This': ", linked_list_map.contains('This'))
    print('total time: {} seconds'.format(time.time() - start_time))

    linked_list_map.add('qiyue', 23)
    linked_list_map.add('bayue', 28)
    linked_list_map.add('shiyue', 89)
    linked_list_map.remove('bayue')
    print(linked_list_map.getter('qiyue'))
    print(linked_list_map.get_size())
    print(linked_list_map.getter('shiyue'))
    linked_list_map.setter("bayue", 200)
    print(linked_list_map.getter('bayue'))


if __name__ == "__main__":
    linked_list_map = LinkedListMap()
    linked_list_map_test(linked_list_map)

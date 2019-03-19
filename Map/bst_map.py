'''
    数据结构--07--映射Map（基于二分搜索树BST实现）
'''
import time
from Map.map_base import MapBase

__author__ = 'Yan'
__date__ = '2018/3/17 15:48'


class BSTMap(MapBase):
    '''
        数据结构--07--映射Map（基于二分搜索树BST实现）
    '''
    class _Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, key, value):
        self.root = self._add(self.root, key, value)

    def _add(self, node, key, value):
        '''
            向以node为根节点的二分搜索树中插入节点，节点的键为key，键对应的值为value，采用递归算法实现
        '''
        if node is None:
            self._size += 1
            return self._Node(key, value)

        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        return node

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        '''
            从以node为根节点的二分搜索树中删除键为key的节点，采用递归算法实现
        '''
        if node is None:
            return None

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                # node的左子树为空
                right_node = node.right
                node.right = None
                self._size -= 1
                return right_node

            elif node.right is None:
                # node的右子树为空
                left_node = node.left
                node.left = None
                self._size -= 1
                return left_node
            else:
                # node的左右子树均不为空
                successor = self._minimum(node.right)
                successor.left = node.left
                successor.right = self._remove_min(node.right)
                node.left = None
                node.right = None
                return successor

    def minimum(self):
        '''
            返回二分搜索树的最小元素值，用户调用的minimum方法，真正处理逻辑在_minimum方法中
        '''
        if self._size == 0:
            raise IndexError("BSTMap is empty")

        return self._minimum(self.root).key

    def _minimum(self, node):
        '''
            返回以node为根节点中最小元素值的节点，最小元素值所在的节点在整棵树的最左下方，采用递归实现
        '''
        if node.left is None:
            return node

        node = self._minimum(node.left)
        return node

    def remove_min(self):
        '''
            删除最小元素所在的节点，并返回最小值，用户调用的remove_min方法，真正处理逻辑在_remove_min方法中
        '''
        ret = self._minimum(self.root)
        self.root = self._remove_min(self.root)
        return ret.key

    def _remove_min(self, node):
        '''
            删除以node为根节点的最小元素值所在节点，并返回新二分搜索树的根节点，采用递归算法实现
            存在两种情况：
                1. 最小元素值所在节点没有右子节点，直接remove即可
                2. 最小元素值所在节点存在右子节点，需要先保存右子节点，并连接上最小元素值所在节点的父节点
        '''
        if node.left is None:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node

        node.left = self._remove_min(node.left)
        return node

    def find_node(self, node, key):
        '''
            在以node为根节点的二分搜索树种查找键为key的节点，并返回，采用递归实现
        '''
        if node is None:
            raise IndexError("key {} is not exist".format(key))

        if key == node.key:
            return node
        elif key < node.key:
            result = self.find_node(node.left, key)
        else:
            result = self.find_node(node.right, key)
        return result

    def getter(self, key):
        node = self.find_node(self.root, key)
        return node.value

    def setter(self, key, value):
        try:
            node = self.find_node(self.root, key)
            node.value = value
        except IndexError:
            self.add(key, value)

    def contains(self, key):
        try:
            self.find_node(self.root, key)
            return True
        except IndexError:
            return False


def bst_map_test(bst_map):
    '''
        测试BSTMap代码书写是否正确
    '''
    with open('shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    start_time = time.time()
    for word in words:
        if bst_map.contains(word):
            bst_map.setter(word, bst_map.getter(word)+1)
        else:
            bst_map.add(word, 1)

    print('total words: ', len(words))
    print("unique words: ", bst_map.get_size())
    print("contains word 'This': ", bst_map.contains('This'))
    print('total time: {} seconds'.format(time.time() - start_time))

    bst_map.remove("This")
    print("contains word 'This' after remove : ", bst_map.contains("This"))
    bst_map.setter("This", 200)
    print("the value of key is 'This' : ", bst_map.getter("This"))


if __name__ == "__main__":
    bst_map = BSTMap()
    bst_map_test(bst_map)

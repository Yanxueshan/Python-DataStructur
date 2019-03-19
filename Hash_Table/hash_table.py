'''
    数据结构--13--HashTable（哈希表）
        1. 哈希表充分体现了算法设计领域的经典思想：空间换时间
        2. 哈希表是时间和空间之间的平衡
        3. 哈希函数的设计是很重要的
        4. “键”通过哈希函数得到的“索引”分布越均匀越好

    哈希函数的设计原则：
        1. 一致性：如果a == b，那么hash(a) == hash(b)
        2. 高效性：计算高效简便
        3. 均匀性：哈希值均匀分布

    哈希函数的设计：
        1. 整数：
            小整数  -->  直接用
            大整数  -->  取模（对一个合理的素数取模）
        2. 字符串 --> 转换成整型
            hash(code) = (c * B^3 + o * B^2 + d * B^1 + e * e^0) % M  -->
            hasn(code) = ((((c * B) + o) * B + d) * B + e) % M  -->
            hash(code) = ((((c % M * B) + o) % M * B + d) % M * B + e) % M
'''
import time
from Array.array import Array
from AVL.avl_map import AVLMap
from AVL.avl_tree import AVLTree
from Binary_Search_Tree.BST import BST

__author__ = 'Yan'
__date__ = '2019/3/19 20:29'


class HashTable:
    '''
        数据结构--13--HashTable（哈希表）
    '''
    def __init__(self, M):
        self._M = M
        self._size = 0
        self._hashtable = Array()
        for i in range(self._M):
            self._hashtable[i] = AVLMap()

    def get_size(self):
        '''
            获取HashTable中元素的个数
        '''
        return self._size

    def _hash(self, key):
        '''
            hash函数，0x7fffffff表示将负数转换成正数
        '''
        return (hash(key) & 0x7fffffff) % self._M

    def add(self, key, value):
        '''
            向HashTable中添加一个元素
        '''
        avl_map = self._hashtable[self._hash(key)]
        if avl_map.contains(key):
            avl_map.set(key, value)
        else:
            avl_map.add(key, value)
            self._size += 1

    def remove(self, key):
        '''
            从HashTable中删除一个元素
        '''
        avl_map = self._hashtable[self._hash(key)]
        if avl_map.contains(key):
            value = avl_map.remove(key)
            self._size -= 1
        else:
            raise KeyError("key {} doesn't exist.".format(key))

        return value

    def get(self, key):
        '''
            获取HashTable中key对应的value
        '''
        return self._hashtable[self._hash(key)].getter(key)

    def set(self, key, value):
        '''
            将HashTable中key对应的值修改为value
        '''
        avl_map = self._hashtable[self._hash(key)]
        if avl_map.contains(key):
            avl_map.setter(key, value)
        else:
            raise KeyError("key {} doesn't exist.".format(key))

    def contains(self, key):
        '''
            查询HashTable中是否存在key
        '''
        return self._hashtable[self._hash(key)].contains(key)


def hash_table_test(hash_table, avl_tree, bst):
    with open('pride-and-prejudice.txt', 'r', encoding='utf-8') as f:
        words = f.read()
    words = words.split()

    # HashTable测试
    start_time = time.time()
    for word in words:
        if hash_table.contains(word):
            hash_table.set(word, 1 + hash_table.get(word))
        else:
            hash_table.add(word, 1)
    for word in words:
        hash_table.contains(word)
    print("HashTable test: ------------------")
    print("total words: ", hash_table.get_size())
    print("frequency of pride: ", hash_table.get('pride'))
    print('frequency of prejudice: ', hash_table.get('prejudice'))
    hash_table.remove('pride')
    print("HashTabel spend time: ", time.time()-start_time)

    # AVL树测试
    start_time = time.time()
    for word in words:
        if avl_tree.contains(word):
            avl_tree.setter(word, 1 + avl_tree.getter(word))
        else:
            avl_tree.add(word, 1)
    for word in words:
        avl_tree.contains(word)
    print("AVL test: ------------------")
    print("total words: ", avl_tree.get_size())
    print("frequency of pride: ", avl_tree.getter('pride'))
    print('frequency of prejudice: ', avl_tree.getter('prejudice'))
    avl_tree.remove('pride')
    print("AVL spend time: ", time.time()-start_time)

    # BST测试
    start_time = time.time()
    for word in words:
        bst.add(word)
    for word in words:
        bst.contains(word)
    print("BST test: ------------------")
    print("total words: ", bst.get_size())
    bst.remove('pride')
    print("BST spend time: ", time.time()-start_time)


if __name__ == "__main__":
    hash_table = HashTable(131071)
    avl_tree = AVLTree()
    bst = BST()
    hash_table_test(hash_table, avl_tree, bst)

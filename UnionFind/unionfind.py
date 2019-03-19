'''
    数据结构--11--UnionFind（并查集）
'''
import time
from random import randint
from UnionFind.unionfind_base import UnionFindBase

__author__ = 'Yan'
__date__ = '2019/3/18 16:47'


class UnionFind1(UnionFindBase):
    '''
        数据结构--11--UnionFind（并查集）--> Quick Find
    '''
    def __init__(self, size):
        self._id = [i for i in range(size)]

    def is_connected(self, p, q):
        '''
            O(1)的时间复制度
        '''
        return self._find(p) == self._find(q)

    def union_elements(self, p, q):
        '''
            O(n)的时间复杂度
        '''
        pid = self._find(p)
        qid = self._find(q)
        if pid == qid:
            return
        for i in range(self.get_size()):
            if self._id[i] == pid:
                self._id[i] = qid

    def get_size(self):
        return len(self._id)

    def _find(self, p):
        '''
            查找元素p所对应的集合编号，O(1)的时间复杂度
        '''
        if p < 0 or p >= self.get_size():
            raise IndexError("index is illegal.")
        return self._id[p]


class UnionFind2(UnionFindBase):
    '''
        数据结构--11--UnionFind（并查集）--> Quick Union(有可能会退化成链表)
        是一棵棵树的形式，孩子指向父亲节点
    '''
    def __init__(self, size):
        '''
            parent[i] = j 表示 i 指向 j
        '''
        self._parent = [i for i in range(size)]

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union_elements(self, p, q):
        '''
            O(h)的时间复杂度，h为p和q节点所在树的深度
        '''
        # p所在树的根节点为p_root
        p_root = self._find(p)
        # q所在树的根节点为q_root
        q_root = self._find(q)

        if p_root == q_root:
            return
        self._parent[p_root] = q_root

    def get_size(self):
        return len(self._parent)

    def _find(self, p):
        '''
            查找元素p所对应的集合编号，O(h)的时间复杂度，h为p节点所在树的深度
        '''
        if p < 0 or p >= self.get_size():
            raise IndexError("index is illegal.")

        # 根节点的特点: parent[p] == p
        while p != self._parent[p]:
            # 不断去查询自己的父亲节点, 直到到达根节点
            p = self._parent[p]

        return p


class UnionFind3(UnionFindBase):
    '''
        数据结构--11--UnionFind（并查集）--> Size Optimize(对UnionFind3的优化，防止退化成链表)
    '''
    def __init__(self, size):
        '''
            parent[i] = j 表示 i 指向 j
        '''
        self._parent = [i for i in range(size)]

        # 维护一个字典，记录i节点所在树的元素个数
        self._count = {}
        for i in range(len(self._parent)):
            self._count[i] = 1

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union_elements(self, p, q):
        '''
            O(h)的时间复杂度，h为p和q节点所在树的深度
        '''
        # p所在树的根节点为p_root
        p_root = self._find(p)
        # q所在树的根节点为q_root
        q_root = self._find(q)

        if p_root == q_root:
            return

        if self._count[p_root] < self._count[q_root]:
            self._parent[p_root] = q_root
            self._count[q_root] += self._count[p_root]
            del self._count[p_root]
        else:
            self._parent[q_root] = p_root
            self._count[p_root] += self._count[q_root]
            del self._count[q_root]

    def get_size(self):
        return len(self._parent)

    def _find(self, p):
        '''
            查找元素p所对应的集合编号，O(h)的时间复杂度，h为p节点所在树的深度
        '''
        if p < 0 or p >= self.get_size():
            raise IndexError("index is illegal.")

        # 根节点的特点: parent[p] == p
        while p != self._parent[p]:
            # 不断去查询自己的父亲节点, 直到到达根节点
            p = self._parent[p]

        return p


class UnionFind4(UnionFindBase):
    '''
        数据结构--11--UnionFind（并查集）--> Rank Optimize(对UnionFind3的优化)
    '''
    def __init__(self, size):
        '''
            parent[i] = j 表示 i 指向 j
        '''
        self._parent = [i for i in range(size)]

        # 维护一个字典，记录i节点所在树的深度h
        self._rank = {}
        for i in range(len(self._parent)):
            self._rank[i] = 1

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union_elements(self, p, q):
        '''
            O(h)的时间复杂度，h为p和q节点所在树的深度
        '''
        # p所在树的根节点为p_root
        p_root = self._find(p)
        # q所在树的根节点为q_root
        q_root = self._find(q)

        if p_root == q_root:
            return

        if self._rank[p_root] < self._rank[q_root]:
            self._parent[p_root] = q_root
        elif self._rank[p_root] > self._rank[q_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[p_root] = q_root
            self._rank[q_root] += 1

    def get_size(self):
        return len(self._parent)

    def _find(self, p):
        '''
            查找元素p所对应的集合编号，O(h)的时间复杂度，h为p节点所在树的深度
        '''
        if p < 0 or p >= self.get_size():
            raise IndexError("index is illegal.")

        # 根节点的特点: parent[p] == p
        while p != self._parent[p]:
            # 不断去查询自己的父亲节点, 直到到达根节点
            p = self._parent[p]

        return p


class UnionFind5(UnionFindBase):
    '''
        数据结构--11--UnionFind（并查集）--> Path Compression(路径压缩，对UnionFind4的优化)
    '''
    def __init__(self, size):
        '''
            parent[i] = j 表示 i 指向 j
        '''
        self._parent = [i for i in range(size)]

        # 维护一个字典，记录i节点所在树的深度h
        self._rank = {}
        for i in range(len(self._parent)):
            self._rank[i] = 1

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union_elements(self, p, q):
        '''
            O(h)的时间复杂度，h为p和q节点所在树的深度
        '''
        # p所在树的根节点为p_root
        p_root = self._find(p)
        # q所在树的根节点为q_root
        q_root = self._find(q)

        if p_root == q_root:
            return

        if self._rank[p_root] < self._rank[q_root]:
            self._parent[p_root] = q_root
        elif self._rank[p_root] > self._rank[q_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[p_root] = q_root
            self._rank[q_root] += 1

    def get_size(self):
        return len(self._parent)

    def _find(self, p):
        '''
            查找元素p所对应的集合编号，O(h)的时间复杂度，h为p节点所在树的深度
        '''
        if p < 0 or p >= self.get_size():
            raise IndexError("index is illegal.")

        # 根节点的特点: parent[p] == p
        while p != self._parent[p]:
            # 路径压缩
            self._parent[p] = self._parent[self._parent[p]]
            # 不断去查询自己的父亲节点, 直到到达根节点
            p = self._parent[p]

        return p


class UnionFind6(UnionFindBase):
    '''
        数据结构--11--UnionFind（并查集）--> Path Compression(路径压缩，对UnionFind5的优化)
    '''
    def __init__(self, size):
        '''
            parent[i] = j 表示 i 指向 j
        '''
        self._parent = [i for i in range(size)]

        # 维护一个字典，记录i节点所在树的深度h
        self._rank = {}
        for i in range(len(self._parent)):
            self._rank[i] = 1

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union_elements(self, p, q):
        '''
            O(h)的时间复杂度，h为p和q节点所在树的深度
        '''
        # p所在树的根节点为p_root
        p_root = self._find(p)
        # q所在树的根节点为q_root
        q_root = self._find(q)

        if p_root == q_root:
            return

        if self._rank[p_root] < self._rank[q_root]:
            self._parent[p_root] = q_root
        elif self._rank[p_root] > self._rank[q_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[p_root] = q_root
            self._rank[q_root] += 1

    def get_size(self):
        return len(self._parent)

    def _find(self, p):
        '''
            查找元素p所对应的集合编号，O(h)的时间复杂度，h为p节点所在树的深度
        '''
        if p < 0 or p >= self.get_size():
            raise IndexError("index is illegal.")

        # 根节点的特点: parent[p] == p
        if p != self._parent[p]:
            # 使用递归实现路径压缩，使得所有节点的深度最大为2
            self._parent[p] = self._find(self._parent[p])

        return self._parent[p]


def union_find_test(union_find, size, m):
    '''
        测试UnionFind代码是否书写正确，以及性能测试
    '''
    start_time = time.time()
    for i in range(m):
        a = randint(0, size-1)
        b = randint(0, size-1)
        union_find.union_elements(a, b)

    for i in range(m):
        a = randint(0, size-1)
        b = randint(0, size-1)
        union_find.is_connected(a, b)

    print("UnionFind: ", time.time() - start_time)


if __name__ == "__main__":
    size = 10000
    m = 10000
    union_find1 = UnionFind1(size)
    union_find2 = UnionFind2(size)
    union_find3 = UnionFind3(size)
    union_find4 = UnionFind4(size)
    union_find5 = UnionFind5(size)
    union_find6 = UnionFind6(size)
    union_find_test(union_find1, size, m)
    union_find_test(union_find2, size, m)
    union_find_test(union_find3, size, m)
    union_find_test(union_find4, size, m)
    union_find_test(union_find5, size, m)
    union_find_test(union_find6, size, m)

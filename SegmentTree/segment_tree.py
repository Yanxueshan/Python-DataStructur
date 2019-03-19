'''
    数据结构--09--线段树（区间树）
    最经典的线段树问题：区间染色
    另一类经典问题：区间查询
'''

__author__ = 'Yan'
__date__ = '2019/3/18 14:47'


class SegmentTree:
    '''
        数据结构--09--线段树（区间树）
    '''
    def __init__(self, arr, merger):
        if not arr or not isinstance(arr, list) or not merger:
            raise ValueError("arr and merger should be passed in.")
        self._data = arr[:]
        self._tree = [None] * (len(arr) * 4)
        self._merger = merger
        self._build_segment_tree(0, 0, len(self._data) - 1)

    def get_size(self):
        '''
            获取形成线段树的list中元素个数
        '''
        return len(self._data)

    def get(self, index):
        '''
            获取形成线段树的list中索引为index的值
        '''
        if index < 0 or index > len(self._data) - 1:
            raise IndexError("index is illegal")
        return self._data[index]

    def _left_child(self, index):
        '''
            返回完全二叉树的list表示中，一个索引所表示的元素的左孩子节点的索引
        '''
        return 2 * index + 1

    def _right_child(self, index):
        '''
            返回完全二叉树的list表示中，一个索引所表示的元素的右孩子节点的索引
        '''
        return 2 * index + 2

    def _build_segment_tree(self, tree_index, left, right):
        '''
            在treeIndex的位置创建表示区间[left...right]的线段树，采用递归实现
        '''
        if left == right:
            self._tree[tree_index] = self._data[left]
            return

        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)

        mid = left + (right - left) // 2
        self._build_segment_tree(left_tree_index, left, mid)
        self._build_segment_tree(right_tree_index, mid+1, right)

        self._tree[tree_index] = self._merger(self._tree[left_tree_index], self._tree[right_tree_index])

    def query(self, query_left, query_right):
        '''
            返回区间[queryL, queryR]的值
        '''
        if query_left < 0 or query_left > len(self._data) - 1 or query_right < 0 or query_right > len(self._data) - 1 or query_left > query_right:
            raise IndexError("query_left or query_right is illegal.")

        return self._query(0, 0, len(self._data) - 1, query_left, query_right)

    def _query(self, tree_index, left, right, query_left, query_right):
        '''
            在以tree_index为根的线段树中[left...right]的范围里，搜索区间[query_left...query_right]的值
        '''
        if left == query_left and right == query_right:
            return self._tree[tree_index]

        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)

        mid = left + (right - left) // 2

        if query_left >= mid + 1:
            return self._query(right_tree_index, mid + 1, right, query_left, query_right)
        elif query_right <= mid:
            return self._query(left_tree_index, left, mid, query_left, query_right)

        left_result = self._query(left_tree_index, left, mid, query_left, mid)
        right_result = self._query(right_tree_index, mid + 1, right, mid + 1, query_right)
        return self._merger(left_result, right_result)

    def set(self, index, value):
        '''
            将index位置的值更新为value
        '''
        if index < 0 or index > len(self._data) - 1:
            raise IndexError("index is illegal")
        self._data[index] = value
        self._set(0, 0, len(self._data) - 1, index, value)

    def _set(self, tree_index, left, right, index, value):
        '''
            在以tree_index为根的线段树中更新index位置的值为value
        '''
        if left == right:
            self._tree[tree_index] = value
            return

        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)

        mid = left + (right - left) // 2
        if index >= mid + 1:
            self._set(right_tree_index, mid + 1, right, index, value)
        else:
            self._set(left_tree_index, left, mid, index, value)

        # 更新当前tree_index位置的值
        self._tree[tree_index] = self._merger(self._tree[left_tree_index], self._tree[right_tree_index])

    def __str__(self):
        result = []
        result.append('[')
        for i in range(len(self._tree)):
            result.append(str(self._tree[i]))
            if i < len(self._tree) - 1:
                result.append(', ')
        result.append(']')
        return ''.join(result)


def merger(value1, value2):
    '''
        merger函数，返回value1和value2两数之和
    '''
    return value1 + value2


def segmrent_tree_test(segment_tree):
    '''
        测试SegmentTree代码书写是否正确
    '''
    print(segment_tree)
    print(segment_tree.query(3, 5))
    segment_tree.set(2, 10)
    print(segment_tree)
    print(segment_tree.query(2, 5))


if __name__ == "__main__":
    data = [1, -2, 9, -4, 8, -3, -8]
    segment_tree = SegmentTree(data, merger)
    segmrent_tree_test(segment_tree)

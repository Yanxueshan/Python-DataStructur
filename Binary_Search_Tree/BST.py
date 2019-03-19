'''
    数据结构--05--二分搜索树（基于ArrayQueue实现）
    二分搜索树：
        1. 每个节点的值都大于其左子树的所有节点的值
        2. 每个节点的值都小于其右子树的所有节点的值
        3. 每个节点的左子树和右子树都是一个二分搜索树（天然的递归）
    * 空也是一个二叉树，一个节点也是一个二叉树，二分搜索树就是一个二叉树
'''
from _Queue.array_queue import ArrayQueue

__author__ = 'Yan'
__date__ = '2018/11/19 22:54'


class BST:
    '''
        数据结构--05--二分搜索树（基于ArrayQueue实现），不包含重复元素
    '''
    class _Node:
        def __init__(self, value=None):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.size = 0

    def get_size(self):
        '''
            返回二分搜索树的节点个数
        '''
        return self.size

    def is_empty(self):
        '''
            判断二分搜索树是否为空
        '''
        return self.size == 0

    def add(self, value):
        '''
            用户真正调用的add方法，真正处理逻辑隐藏在_add方法中
        '''
        self.root = self._add(self.root, value)

    def _add(self, node, value):
        '''
            向以node为根节点的二分搜索树种添加值为value的节点，采用递归算法
        '''
        add_node = self._Node(value)

        # 递归到底的情况
        if node is None:
            self.size += 1
            return add_node

        # 若value存在当前二分搜索树中，则不再添加，直接返回当前node
        if value < node.value:
            node.left = self._add(node.left, value)
        elif value > node.value:
            node.right = self._add(node.right, value)

        return node

    def contains(self, value):
        '''
            用户真正调用的contains方法，真正处理逻辑隐藏在_contains方法中
            查询二分搜索树中是否包含值为value的节点，如果包含则返回True，否则返回False
        '''
        return self._contains(self.root, value)

    def _contains(self, node, value):
        '''
            查询以node为根节点的二分搜索树中是否存在值为value的节点，存在返回True，否则返回False
            采用递归算法实现
        '''
        if node is None:
            return False

        if value == node.value:
            return True
        elif value < node.value:
            return self._contains(node.left, value)
        else:
            return self._contains(node.right, value)

    def pre_order(self):
        '''
            前序遍历，用户真正调用的pre_order方法，真正的处理逻辑隐藏在_pre_order方法中
        '''
        self._pre_order(self.root)

    def _pre_order(self, node):
        '''
            前序遍历（深度优先遍历）以node为根节点的二分搜索树，采用递归算法实现
        '''
        if node is None:
            return

        print(node.value)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def in_order(self):
        '''
            中序遍历，用户调用的in_order方法，真正处理逻辑隐藏在_in_order方法中
        '''
        self._in_order(self.root)

    def _in_order(self, node):
        '''
            中序遍历以node为根节点的二分搜索树，采用递归算法实现
        '''
        if node is None:
            return

        self._in_order(node.left)
        print(node.value)
        self._in_order(node.right)

    def post_order(self):
        '''
            后序遍历，用户调用的post_order方法，真正处理逻辑隐藏在_post_order方法中
       '''
        self._post_order(self.root)

    def _post_order(self, node):
        '''
            后序遍历以node为根节点的二分搜索树，采用递归算法实现
        '''
        if node is None:
            return

        self._post_order(node.left)
        self._post_order(node.right)
        print(node.value)

    def level_order(self):
        '''
            层序遍历（广度优先遍历），使用辅助数据结构队列ArrayQueue实现
        '''
        result = []
        queue = ArrayQueue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.get_front()
            result.append(queue.dequeue().value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        print("level_order: ", ' '.join("%s" % value for value in result))

    def minimum(self):
        '''
            返回二分搜索树的最小元素值，用户调用的minimum方法，真正处理逻辑在_minimum方法中
        '''
        if self.size == 0:
            raise IndexError("BST is empty")

        return self._minimum(self.root).value

    def _minimum(self, node):
        '''
            返回以node为根节点中最小元素值的节点，最小元素值所在的节点在整棵树的最左下方
        '''
        if node.left is None:
            return node

        return self._minimum(node.left)

    # 寻找二分搜索树的最大元素
    def maximum(self):
        '''
            返回二分搜索树的最大元素值，用户调用的maximum方法，真正处理逻辑在_maximum方法中
        '''
        if self.size == 0:
            raise IndexError("BST is empty")

        return self._maximum(self.root).value

    def _maximum(self, node):
        '''
            返回以node为根节点中最大元素值的节点，最大元素值所在的节点在整棵树的最右下方
        '''
        if node.right is None:
            return node

        return self._maximum(node.right)

    def remove_min(self):
        '''
            删除最小元素所在的节点，并返回最小值，用户调用的remove_min方法，真正处理逻辑在_remove_min方法中
        '''
        ret = self.minimum()
        self.root = self._remove_min(self.root)
        return ret

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
            self.size -= 1
            return right_node

        node.left = self._remove_min(node.left)
        return node

    def remove_max(self):
        '''
            删除最大元素所在的节点，并返回最大值，用户调用的remove_max方法，真正处理逻辑在_remove_max方法中
        '''
        ret = self.maximum()
        self.root = self._remove_max(self.root)
        return ret

    def _remove_max(self, node):
        '''
            删除以node为根节点的最大元素值所在节点，并返回新二分搜索树的根节点，采用递归算法实现
            存在两种情况：
                1. 最大元素值所在节点没有左子节点，直接remove即可
                2. 最大元素值所在节点存在左子节点，需要先保存左子节点，并连接上最大元素值所在节点的父节点
        '''
        if node.right is None:
            left_node = node.left
            node.left = None
            self.size -= 1
            return left_node

        node.right = self._remove_max(node.right)
        return node

    def remove(self, value):
        '''
            删除值为value的节点，用户调用的方法，真正处理逻辑隐藏在_remove方法中
        '''
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        '''
            删除以node为根节点的二分搜索树中值为value的节点，并返回新二分搜索树的根节点，采用递归算法实现
        '''
        if node is None:
            return None

        if node.value == value:
            if node.left is None:
                # 待删除的节点node左子树为空，先保存node的右子树
                right_node = node.right
                node.right = None
                self.size -= 1
                return right_node
            elif node.right is None:
                # 待删除的节点右子树为空，先保存node的左子树
                left_node = node.left
                node.left = None
                self.size -= 1
                return left_node
            else:
                # 待删除的节点node左子树和右子树均不为空
                # 1. 找到node的右子树的最小元素所在的节点，并赋给successor
                successor = self._minimum(node.right)
                # 2. 删除node的右子树的最小元素所在的节点，self._remove_min(node.right)返回的
                #    是以node.right为根节点的二分搜索树删除最小元素后的新二分搜索树的根节点，赋值
                #    给successor.right
                successor.right = self._remove_min(node.right)
                # 不用维护size，因为self._remove_min(node.right)中size已经-1了
                successor.left = node.left

                node.left = None
                node.right = None
                return successor

        elif value < node.value:
            node.left = self._remove(node.left, value)
        else:
            node.right = self._remove(node.right, value)

        return node


def print_test(bst):
    '''
        print test
    '''
    print("pre_order: --------------")
    bst.pre_order()
    print("in_order: ---------------")
    bst.in_order()
    print("post_order: -------------")
    bst.post_order()
    bst.level_order()
    print("minimum: ", bst.minimum())
    print("maximum: ", bst.maximum())


def bst_test():
    '''
        测试BST代码是否书写正确
    '''
    bst = BST()
    bst.add(25)
    bst.add(20)
    bst.add(18)
    bst.add(19)
    bst.add(67)
    bst.add(30)
    print_test(bst)

    print("after remove min and max: -------- ")
    bst.remove_min()
    bst.remove_max()
    print_test(bst)

    print("after remove 25: -----------------")
    bst.remove(25)
    print_test(bst)


if __name__ == "__main__":
    bst_test()

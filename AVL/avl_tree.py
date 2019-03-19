'''
    数据结构--12--AVL树（平衡二叉树）
        1. 定义：叶子节点之间的deepth差不大于1（对于任一节点，左子树和右子树的高度差不大于1）
        2. 常见AVL树：满二叉树/完全二叉树/线段树/堆...
        3. 平衡二叉树的高度和节点数量之间的关系为log2n
        4. 平衡因子：左右子树的高度差
'''
import time
from Binary_Search_Tree.BST import BST

__author__ = 'Yan'
__date__ = '2019/3/19 10:47'


class AVLTree:
    '''
        数据结构--12--AVL树
    '''
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        '''
            获取AVL树中元素个数
        '''
        return self._size

    def is_empty(self):
        '''
            判断AVL树是否为空
        '''
        return self._size == 0

    def is_banlanced(self):
        '''
            判断该二叉树是否是一棵AVL树
        '''
        return self._is_banlanced(self._root)

    def _is_banlanced(self, node):
        '''
            判断该二叉树是否是一棵AVL树，采用递归实现
        '''
        if node is None:
            return True
        banlance_factor = self._get_banlance_factor(node)
        if abs(banlance_factor) > 1:
            return False
        return self._is_banlanced(node.left) and self._is_banlanced(node.right)

    def is_bst(self):
        '''
            判断该二叉树是否是一棵二分搜索树，二分搜索树的中序遍历得到的数据是有序的
        '''
        result = []
        self._in_order(self._root, result)

        for i in range(1, len(result)):
            if result[i - 1] > result[i]:
                return False
        return True

    def _in_order(self, node, result):
        '''
            对该二叉树进行中序遍历
        '''
        if node is None:
            return

        self._in_order(node.left, result)
        result.append(node.key)
        self._in_order(node.right, result)

    def _get_height(self, node):
        '''
            获取节点node的高度
        '''
        if node is None:
            return 0
        return node.height

    def _get_banlance_factor(self, node):
        '''
            获取节点node的平衡因子
        '''
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def add(self, key, value):
        '''
            向AVL树中添加一个元素(key, value)
        '''
        self._root = self._add(self._root, key, value)

    def _add(self, node, key, value):
        '''
            向以node为根节点的AVL树中添加一个元素(key, value)
        '''
        if node is None:
            self._size += 1
            return self._Node(key, value)

        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        else:
            node.value = value

        # 更新node.height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # 计算平衡因子
        banlance_factor = self._get_banlance_factor(node)

        # 维护平衡
        # 插入的元素在左侧的左侧
        if banlance_factor > 1 and self._get_banlance_factor(node.left) >= 0:
            return self._right_rotate(node)

        # 插入的元素在右侧的右侧
        if banlance_factor < -1 and self._get_banlance_factor(node.right) <= 0:
            return self._left_rotate(node)

        # 插入的元素在左侧的右侧
        if banlance_factor > 1 and self._get_banlance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # 插入的元素在右侧的左侧
        if banlance_factor < -1 and self._get_banlance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _right_rotate(self, node):
        '''
            在y节点的左子树的左侧中加入一个元素后，导致不平衡 ---> 右旋转，维护平衡

                    y                              x
                   / \                           /   \
                  x   T4     向右旋转 (y)        z     y
                 / \       - - - - - - - ->    / \   / \
                z   T3                       T1  T2 T3 T4
               / \
             T1   T2

            假设 T1 和 T2 子树的最大高度为 h --> 那么 z 的高度为 h+1 --> x 的高度为 h+2
            --> 因为 x 也是保持平衡的，所以 T3 的 高度为 h+1 或者 h
            --> y 打破平衡，由于 x 的高度为 h+2，所以 T4 的高度为 h

            按照这样计算，旋转后的二分搜索树也是维持平衡的
        '''
        x = node.left
        T3 = x.right
        x.right = node
        node.left = T3

        # 更新height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _left_rotate(self, node):
        '''
            在y节点的右子树的右侧中加入一个元素后，导致不平衡 --> 左旋转，维护平衡

                y                             x
              /  \                          /   \
             T1   x      向左旋转 (y)       y     z
                 / \   - - - - - - - ->   / \   / \
               T2  z                     T1 T2 T3 T4
                  / \
                 T3 T4
        '''
        x = node.right
        T2 = x.left
        x.left = node
        node.right = T2

        # 更新height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _get_node(self, node, key):
        '''
            返回以node为根节点的AVL树中，key所在的node
        '''
        if node is None:
            return None

        if key < node.key:
            return self._get_node(node.left, key)
        elif key > node.key:
            return self._get_node(node.right, key)
        else:
            return node

    def contains(self, key):
        '''
            查询AVL树中是否存在键为key的节点
        '''
        ret = self._get_node(self._root, key)
        if ret is None:
            return False
        return True

    def getter(self, key):
        '''
            获取AVL树中key对应的值
        '''
        ret = self._get_node(self._root, key)
        if ret is None:
            raise KeyError("AVL Tree has no key : {}".format(key))
        return ret.value

    def setter(self, key, value):
        '''
            将AVL树中key对应的value修改为value，如果不存在key，则添加一个新node
        '''
        ret = self._get_node(self._root, key)
        if ret is None:
            self.add(key, value)
            return
        ret.value = value

    def remove(self, key):
        '''
            删除AVL树中key所在的节点
        '''
        node = self._get_node(self._root, key)
        if node is not None:
            self._root = self._remove(self._root, key)
            return node.value
        return None

    def _remove(self, node, key):
        '''
            删除以node为根节点的AVL树中key所在的节点
        '''
        ret_node = None
        if node is None:
            return None

        if node.key == key:
            if node.left is None:
                # 待删除的节点node左子树为空，先保存node的右子树
                right_node = node.right
                node.right = None
                self._size -= 1
                ret_node = right_node
            elif node.right is None:
                # 待删除的节点右子树为空，先保存node的左子树
                left_node = node.left
                node.left = None
                self._size -= 1
                ret_node = left_node
            else:
                # 待删除的节点node左子树和右子树均不为空
                # 1. 找到node的右子树的最小元素所在的节点，并赋给successor
                successor = self._minimum(node.right)
                # 2. 删除node的右子树的最小元素所在的节点，self._remove_min(node.right)返回的
                #    是以node.right为根节点的二分搜索树删除最小元素后的新二分搜索树的根节点，赋值
                #    给successor.right
                if successor is not None:
                    successor.right = self._remove(node.right, successor.key)
                    successor.left = node.left
                    self._size -= 1

                    node.left = None
                    node.right = None
                ret_node = successor

        elif key < node.key:
            node.left = self._remove(node.left, key)
        else:
            node.right = self._remove(node.right, key)

        if ret_node is None:
            return None

        # 更新node.height
        ret_node.height = 1 + max(self._get_height(ret_node.left), self._get_height(ret_node.right))

        # 计算平衡因子
        banlance_factor = self._get_banlance_factor(ret_node)

        # 维护平衡
        # 插入的元素在左侧的左侧
        if banlance_factor > 1 and self._get_banlance_factor(ret_node.left) >= 0:
            return self._right_rotate(ret_node)

        # 插入的元素在右侧的右侧
        if banlance_factor < -1 and self._get_banlance_factor(ret_node.right) <= 0:
            return self._left_rotate(ret_node)

        # 插入的元素在左侧的右侧
        if banlance_factor > 1 and self._get_banlance_factor(ret_node.left) < 0:
            ret_node.left = self._left_rotate(ret_node.left)
            return self._right_rotate(ret_node)

        # 插入的元素在右侧的左侧
        if banlance_factor < -1 and self._get_banlance_factor(ret_node.right) > 0:
            ret_node.right = self._right_rotate(ret_node.right)
            return self._left_rotate(ret_node)

        return ret_node

    def minimum(self):
        '''
            返回AVL树中最小key的node
        '''
        return self._minimum(self._root)

    def _minimum(self, node):
        '''
            返回AVL树中最小key的node
        '''
        if node.left is None:
            return node
        self._minimum(node.left)


def avl_tree_test(avl_tree, bst):
    '''
        测试AVL树代码是否书写正确，以及性能测试
    '''
    with open('pride-and-prejudice.txt', 'r', encoding='utf-8') as f:
        words = f.read()
    words = words.split()

    # AVL树测试
    start_time = time.time()
    for word in words:
        if avl_tree.contains(word):
            avl_tree.setter(word, 1 + avl_tree.getter(word))
        else:
            avl_tree.add(word, 1)

    print("total words: ", avl_tree.get_size())
    print("frequency of pride: ", avl_tree.getter('pride'))
    print('frequency of prejudice: ', avl_tree.getter('prejudice'))

    # print("is BST: ", avl_tree.is_bst())
    # print("is Banlanced: ", avl_tree.is_banlanced())

    avl_tree.remove('pride')
    print("AVL spend time: ", time.time()-start_time)
    # print("is BST: ", avl_tree.is_bst())
    # print("is Banlanced: ", avl_tree.is_banlanced())

    # BST测试
    start_time = time.time()
    for word in words:
        bst.add(word)

    print("total words: ", bst.get_size())

    bst.remove('pride')
    print("BST spend time: ", time.time()-start_time)


if __name__ == "__main__":
    avl_tree = AVLTree()
    bst = BST()
    avl_tree_test(avl_tree, bst)

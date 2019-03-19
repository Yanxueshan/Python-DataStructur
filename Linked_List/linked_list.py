'''
    数据结构--02--链表
'''
__author__ = 'Yan'
__date__ = '2018/11/19 21:39'


class LinkedList:
    '''
        数据结构--02--链表
    '''

    class _Node:
        '''
            表示链表中的每个节点
        '''
        def __init__(self, value=None, node_next=None):
            '''
                value : 当前节点的值
                node_next : 指向的下个节点
            '''
            self.value = value
            self.next = node_next

    def __init__(self):
        '''
            构造函数，dummy_head : 虚拟头指针
        '''
        self.dummy_head = self._Node()
        self.size = 0

    def get_size(self):
        '''
            获取链表的节点个数
        '''
        return self.size

    def is_empty(self):
        '''
            判断链表是否为空
        '''
        return self.size == 0

    def add_first(self, value):
        '''
            在链表首部添加一个元素，值为value
        '''
        self.add(0, value)

    def add_last(self, value):
        '''
            在链表末尾添加一个元素，值为value
        '''
        self.add(self.size, value)

    def add(self, index, value):
        '''
            在索引为index的位置添加一个元素，值为value
        '''
        if index < 0 or index > self.size:
            raise IndexError("Add failed, Required index >= 0 and index <= %s" % self.size)

        # 找到要插入的位置的前一个节点
        pre = self.dummy_head
        for i in range(index):
            pre = pre.next

        add_node = self._Node(value=value)
        add_node.next = pre.next
        pre.next = add_node

        self.size += 1

    def get(self, index):
        '''
            获取索引为index的元素的值
        '''
        if self.size == 0:
            raise IndexError("linked_list is empty")
        if index < 0 or index >= self.size:
            raise IndexError("Add failed, Required index >= 0 and index < %s" % self.size)

        cur = self.dummy_head
        for i in range(index + 1):
            cur = cur.next
        return cur.value

    def get_first(self):
        '''
            获取链表第一个元素的值
        '''
        return self.get(0)

    def get_last(self):
        '''
            获取链表最后一个元素的值
        '''
        return self.get(self.size - 1)

    def set(self, index, value):
        '''
            将链表索引为index位置的元素值修改为value
        '''
        if self.size == 0:
            raise IndexError("linked_list is empty")
        if index < 0 or index >= self.size:
            raise IndexError("Set failed, Required index >= 0 and index < %s" % self.size)

        cur = self.dummy_head
        for i in range(index + 1):
            cur = cur.next
        cur.value = value

    def contains(self, value):
        '''
            查询链表中是否存在值为value的元素，如果不存在，则返回-1
        '''
        cur = self.dummy_head.next
        for i in range(self.size):
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def remove(self, index):
        '''
            删除链表中索引为index位置的节点，并返回节点的值
        '''
        if self.size == 0:
            raise IndexError("linked_list is empty")
        if index < 0 or index >= self.size:
            raise IndexError("Remove failed, Required index >= 0 and index < %s" % self.size)

        pre = self.dummy_head
        for i in range(index):
            pre = pre.next

        remove_node = pre.next
        ret = remove_node.value
        pre.next = remove_node.next
        remove_node.next = None
        self.size -= 1

        return ret

    def remove_first(self):
        '''
            删除链表的第一个节点，并返回节点的值
        '''
        return self.remove(0)

    def remove_last(self):
        '''
            删除链表的最后一个节点，并返回节点的值
        '''
        return self.remove(self.size - 1)

    def remove_element(self, value):
        '''
            删除链表中值为value的节点
        '''
        cur = self.dummy_head
        for i in range(self.size):
            if cur.next is not None:
                cur = cur.next
                if cur.value == value:
                    self.remove(i)
                    break
        else:
            raise ValueError("The node whose value is {0} does not exist".format(value))


def linked_list_print(linked_list):
    '''
        打印链表中所有节点的值
    '''
    linked_list_value = []
    for i in range(linked_list.size):
        linked_list_value.append(linked_list.get(i))

    print(linked_list_value)


if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(10):
        linked_list.add_last(i)

    linked_list_print(linked_list)
    linked_list.add(8, "shiyue")
    linked_list_print(linked_list)

    linked_list.remove_element(3)
    linked_list_print(linked_list)

    print(linked_list.contains("shiyue"))
    print(linked_list.contains("jiuyue"))

    linked_list.set(7, "liuyue")
    linked_list_print(linked_list)

    linked_list.remove_element("jiuyue")
    linked_list_print(linked_list)

'''
    数据结构--01--数组
'''
__author__ = 'Yan'
__date__ = '2018/11/19 16:13'


class Array:
    '''
        数据结构--01--数组
    '''
    def __init__(self, arr=None, capacity=10):
        if isinstance(arr, list):
            self._data = arr[:]
            self._size = len(arr)
        else:
            self._size = 0
            self._data = [None] * capacity

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, key, value):
        self.add_last(value)

    def get_capacity(self):
        '''
            获取数组的容量
        '''
        return len(self._data)

    def get_size(self):
        '''
            获取数组中的元素个数
        '''
        return self._size

    def is_empty(self):
        '''
            判断数组是否为空
        '''
        return self._size == 0

    def add_last(self, value):
        '''
            在数组末尾插入元素value
        '''
        self.add(self._size, value)

    def add_first(self, value):
        '''
            在数组起始位置插入元素value
        '''
        self.add(0, value)

    def add(self, index, value):
        '''
            在索引为index的位置插入元素value
        '''

        if index < 0 or index > self._size:
            raise IndexError("Add failed, Required index >= 0 and index <= size")

        # 如果数组full，那么扩容一倍
        if self._size == len(self._data):
            if self._size == 0:
                self._resize(1)
            else:
                self._resize(len(self._data) * 2)

        # index之后的元素往后移一位
        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]

        self._data[index] = value
        self._size += 1

    def get_first(self):
        '''
            获取第0个元素的值
        '''
        return self.get(0)

    def get_last(self):
        '''
            获取最后一个元素的值
        '''
        return self.get(self._size - 1)

    def get(self, index):
        '''
            获取索引为index的值
        '''
        if index < 0 or index >= self._size:
            raise IndexError("get failed, Required index >= 0 and index <= size")
        return self._data[index]

    def set(self, index, value):
        '''
            将索引为index的值改为value
        '''
        if index < 0 or index >= self._size:
            raise IndexError("set failed, Required index >= 0 and index <= size")
        self._data[index] = value

    def contains(self, value):
        '''
            查看数组中是否包含元素value，包含则返回True，否则返回False
        '''
        for i in range(self._size):
            if self._data[i] == value:
                return True
        return False

    def find_index(self, value):
        '''
            查找元素值为value在数组中的索引，如果不存在，则返回-1
        '''
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1

    def remove_first(self):
        '''
            移除数组中第一个元素
        '''
        return self.remove(0)

    def remove_last(self):
        '''
            删除数组中最后一个元素
        '''
        return self.remove(self._size - 1)

    def remove_element(self, value):
        '''
            删除数组中值为value的元素
        '''
        index = self.find_index(value)
        self.remove(index)

    def remove(self, index):
        '''
            从数组中删除索引为index的元素，并返回删除的元素值
        '''
        if index < 0 or index > self._size:
            raise IndexError("remove failed, Required index >= 0 and index < size")

        ret = self._data[index]

        # index之后的元素往前移动一位
        for i in range(index + 1, self._size):
            self._data[i - 1] = self._data[i]
        self._size -= 1

        # 如果数组元素小于容量的1/4，则缩小容量至原有的1/2
        if self._size < len(self._data) // 4 and len(self._data) // 2 != 0:
            self._resize(len(self._data) // 2)
        return ret

    def _resize(self, new_capacity):
        '''
            将数组空间的容量变成new_capacity的大小
        '''
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def swap(self, i, j):
        '''
            交换索引为i和j两个位置的值
        '''
        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            raise IndexError("index is illegal")
        self._data[i], self._data[j] = self._data[j], self._data[i]


if __name__ == "__main__":
    array = Array()
    for i in range(10):
        array.add_last(i)
    print("capacity: %d" % array.get_capacity())
    print("size: %d" % array.get_size())

    array.add_last(10)
    print("capacity: %d" % array.get_capacity())
    print("size: %d" % array.get_size())

    array.add(4, "shiyue")

    print(array.find_index("shiyue"))

    for i in range(array.get_size()):
        print(array.get(i))

    for i in range(8):
        array.remove_last()
    print("capacity: %d" % array.get_capacity())
    print("size: %d" % array.get_size())

'''
    数据结构--03--循环队列
'''
from _Queue.queue_base import QueueBase

__author__ = 'Yan'
__date__ = '2018/11/19 20:26'


class LoopQueue(QueueBase):
    '''
        数据结构--03--循环队列
    '''
    # capacity = 10时，size最大为9，会浪费一个空间
    def __init__(self, capacity=10):
        self._data = [None] * (capacity + 1)
        self.front = 0
        self.tail = 0
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        '''
            当self.front == self.tail时循环队列也为空
        '''
        return self.size == 0

    # 入队，当front == tail时，队列为空；当(tail + 1) % capacity == front时为满
    # tail 指向队尾最后一个空的位置
    # front 指向队首
    def enqueue(self, value):
        if (self.tail + 1) % len(self._data) == self.front:
            self._resize(2 * self.get_capacity())

        self._data[self.tail] = value
        self.tail = (self.tail + 1) % len(self._data)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise ValueError("dequeue failed, queue is empty")

        ret = self._data[self.front]
        self._data[self.front] = None
        self.front = (self.front + 1) % len(self._data)
        self.size -= 1

        if self.size < self.get_capacity() // 4 and self.get_capacity() // 2 != 0:
            self._resize(self.get_capacity() // 2)

        return ret

    def get_front(self):
        if self.size == 0:
            raise ValueError("dequeue failed, queue is empty")
        return self._data[self.front]

    def get_capacity(self):
        '''
            获取队列的空间容量
        '''
        return len(self._data) - 1

    def _resize(self, new_capacity):
        '''
            将队列的容量设置为new_capacity
        '''
        new_data = [None] * (new_capacity + 1)
        for i in range(self.size):
            new_data[i] = self._data[(self.front + i) % len(self._data)]
        self._data = new_data
        self.front = 0
        self.tail = self.size


def loop_queue_test():
    '''
        测试循环队列代码是否正确
    '''
    queue = LoopQueue()
    for i in range(10):
        queue.enqueue(i)
    print("capacity: %d" % queue.get_capacity())
    print("size: %d" % queue.get_size())
    queue.enqueue("a")
    print("capacity: %d" % queue.get_capacity())
    print("size: %d" % queue.get_size())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.get_front())

    for i in range(8):
        queue.dequeue()
    print("capacity: %d" % queue.get_capacity())
    print("size: %d" % queue.get_size())


if __name__ == "__main__":
    loop_queue_test()

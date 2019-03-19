'''
    数据结构--10--Trie（字典树/前缀树）
'''

__author__ = 'Yan'
__date__ = '2019/3/18 16:47'


class Trie:
    '''
        数据结构--10--Trie（字典树/前缀树）
    '''
    class _Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = [None] * 26

    def __init__(self):
        self._root = self._Node()
        self._size = 0

    def get_size(self):
        '''
            返回Trie中单词的个数
        '''
        return self._size

    def add(self, word):
        '''
            向Trie中添加一个单词word
        '''
        cur = self._root
        for letter in word:
            # 获取字母letter在next中的index，next中包含26个字母
            index = ord(letter.lower()) - ord('a')

            # 如果letter所在的index为None，则新创建一个Node
            if cur.next[index] is None:
                cur.next[index] = self._Node()
            cur = cur.next[index]

        if cur.is_word is False:
            cur.is_word = True
            self._size += 1

    def contains(self, word):
        '''
            查询Trie中是否包含单词word，包含则返回True，否则返回False
        '''
        cur = self._root
        for letter in word:
            index = ord(letter.lower()) - ord('a')
            if cur.next[index] is None:
                return False
            cur = cur.next[index]

        return cur.is_word

    def is_prefix(self, prefix):
        '''
            查询Trie中是否存在单词是以prefix为前缀，存在返回True，否则返回False
        '''
        cur = self._root
        for letter in prefix:
            index = ord(letter.lower()) - ord('a')
            if cur.next[index] is None:
                return False
            cur = cur.next[index]
        return True


def trie_test(trie):
    '''
        测试Trie代码是否书写正确
    '''
    words = ['liuyue', 'qiyue', 'bayue', 'jiuyue', 'shiyue', 'bayuechangan']
    for word in words:
        trie.add(word)

    print("contains shiyue: ", trie.contains('shiyue'))
    print('contains shi: ', trie.contains('shi'))
    print('contains panda: ', trie.contains('panda'))
    print('contains prefix shi: ', trie.is_prefix('shi'))


if __name__ == "__main__":
    trie = Trie()
    trie_test(trie)

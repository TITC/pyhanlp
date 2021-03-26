# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-25 17:25
# 《自然语言处理入门》2.4 字典树
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
import sys,os# environment, adjust the priority
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

class Node(object):
    def __init__(self, value) -> None:
        self._children = {}
        self._value = value

    def _add_child(self, char, value, overwrite=False):
        child = self._children.get(char)
        if child is None:
            child = Node(value)
            self._children[char] = child
        elif overwrite:
            child._value = value
        return child


class Trie(Node):
    def __init__(self) -> None:
        super().__init__(None)

    def __contains__(self, key):
        return self[key] is not None

    def __getitem__(self, key):
        state = self
        for char in key:
            state = state._children.get(char)
            if state is None:
                return None
        return state._value

    def __setitem__(self, key, value):
        state = self
        for i, char in enumerate(key):
            if i < len(key) - 1:
                state = state._add_child(char, None, False)
            else:
                state = state._add_child(char, value, True)

if __name__ == '__main__':
    trie = Trie()
    # 增
    trie['自然'] = 'nature'#一开始''，然后存入 自 ，value为Node，不可覆写。然后到 然 ，value为nature，可覆写
    #_add_child 由于 自 两个字已经在字典树中，所以不添加，由于也不可覆写，所以不作处理。而 然 由于可覆写，所以值为value，但由于setitem中传入的是none，所以还是none，而人不在字典树中，所以创建一个
    trie['自然人'] = 'human'
    trie['自然语言'] = 'language'
    trie['自语'] = 'talk	to oneself'
    trie['入门'] = 'introduction'
    assert '自然' in trie
    # 删
    trie['自然'] = None
    assert '自然' not in trie
    # 改
    trie['自然语言'] = 'human language'
    assert trie['自然语言'] == 'human language'
    # 查
    assert trie['入门'] == 'introduction'

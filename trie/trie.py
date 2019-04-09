# -*- coding:utf -*-

class TrieNode(object):

    def __init__(self, data, char_sz=26):
        self.next = [None] * char_sz
        self.data = data
        self.isEndingChar = False


def insert_into_trie(root, string):
    p = root
    for ch in string:
        ind = ord(ch) - ord('a')
        if p.next[ind] is None:
            p.next[ind] = TrieNode(ch)
        p = p.next[ind]
    p.isEndingChar = True


def build_trie_from_strings(strings):
    root = TrieNode('/')
    for s in strings:
        insert_into_trie(root, s)
    return root


def match_string_from_trie(root, string):
    p = root
    for ch in string:
        ind = ord(ch) - ord('a')
        if p.next[ind] is None:
            return False
        p = p.next[ind]
    return p.isEndingChar


if __name__ == '__main__':
    strings = ["hello", "her", "she", "the"]
    root = build_trie_from_strings(strings)
    print(match_string_from_trie(root, 'she'))
    print(match_string_from_trie(root, 'he'))
    print(match_string_from_trie(root, 'hello'))


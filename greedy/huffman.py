# -*- coding:utf-8 -*-


import heapq
from collections import Counter


class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def huffman_encode(inputs):
    q = []
    counter = list(Counter(inputs).items())
    for char, freq in counter:
        heapq.heappush(q, (freq, char))
    lchild = rchild = parent = None
    while len(q) > 0:
        e1 = heapq.heappop(q)
        e2 = heapq.heappop(q)
        if not lchild:
            lchild = Node(e1[1])
        rchild = Node(e2[1])
        parent = Node(None)
        parent.left = lchild
        parent.right = rchil2
        if len(q) != 0:
            heapq.heappush(q, (e1[0] + e2[0], None))
        

        

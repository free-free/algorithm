# -*- coding:utf-8 -*-

import numpy as np


class MaxHeap(object):


    def __init__(self, sz, data):
        self.sz = sz
        self.cnt = len(data)
        self.heap = [0] * (self.sz + 1)
        self.heap[1 : self.cnt] = data
        self.build_heap()

    def build_heap(self):
        last_no_leaf = self.cnt // 2
        for i in range(last_no_leaf, 0, -1):
            self.heaplify(self.heap, self.cnt, i)

    def heaplify(self, heap, cnt, ind):
        while True:
            max_pos = ind
            if 2 * ind <= cnt and heap[2 * ind] > heap[max_pos]:
                max_pos = 2 * ind
            if (2 * ind + 1) <= cnt and heap[2 * ind + 1] > heap[max_pos]:
                max_pos = 2 * ind + 1
            if max_pos == ind:
                break
            heap[max_pos], heap[ind] = heap[ind], heap[max_pos]
            ind = max_pos

    def remove_max(self):
        if self.cnt == 0:
            return -1
        max_val = self.heap[1]
        self.heap[1] = self.heap[self.cnt]
        self.heap[self.cnt] = 0
        self.cnt -= 1
        self.heaplify(self.heap, self.cnt, 1)
        return max_val

    def insert(self, item):
        if self.cnt >= self.sz:
            return -1
        self.cnt += 1
        self.heap[self.cnt] = item
        i = self.cnt 
        while (i // 2) > 0 and self.heap[i // 2] < self.heap[i]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2

def heap_sort(data):
    heap = MaxHeap(len(data), data)
    k = heap.cnt
    while k >= 1:
        heap.heap[1], heap.heap[k] = heap.heap[k], heap.heap[1]
        k -= 1
        heap.heaplify(heap.heap, k, 1)
    return heap.heap[1 : heap.cnt]


if __name__ == '__main__':
    data = np.random.randint(0, 100, 10)
    print(data)
    print(heap_sort(data))
#    heap = MaxHeap(20, data)
#    print(heap.heap)
#    print(heap.remove_max())
#    print(heap.heap)
#    heap.insert(1000)
#    print(heap.heap)


# -*- coding:utf-8 -*-


import numpy as np


class ArrayHeap(object):


    def __init__(self, sz, data = None):
        self.sz  = sz
        self.cnt = 0
        self.heap = [0 for i in range(sz + 1)]
        if data is not None:
            for i, val in enumerate(data):
                self.heap[i + 1] = val
            self.cnt = len(data)
            self._build_heap()
        
    def _build_heap(self):
        last_non_leaf = self.cnt // 2
        for x in range(last_non_leaf, 0, -1):
            max_pos = x
            i = x
            while True:
                if i <= self.cnt and self.heap[i] < self.heap[2 *i ]:
                    max_pos = 2 * i
                if i <= self.cnt and self.heap[max_pos] < self.heap[2 * i + 1]:
                    max_pos = 2 * i + 1
                if max_pos == i:
                    break
                self.heap[i], self.heap[max_pos] = self.heap[max_pos], self.heap[i]
                i = max_pos

                
    

if __name__ == '__main__':
    data = np.random.randint(0, 100, 10)
    print(data)
    heap = ArrayHeap(100, data)
    print(heap.heap)

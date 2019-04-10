# -*- coding:utf-8 -*-


import numpy as np


class MaxHeap(object):


    def __init__(self, sz, data):
        self.sz  = sz
        self.heap = [0] * (sz + 1)
        self.cnt = len(data)
        self.heap[1: self.cnt + 1] = data
        self.build_heap()
        
    def build_heap(self):
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
    heap = MaxHeap(100, data)
    print(heap.heap)

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
        for i in range(last_non_leaf, 0, -1):
            self.heapify(self.heap, self.sz, i)

    def heapify(self, heap, sz, ele_ind):
        while True:
            max_pos = ele_ind
            if  2 * ele_ind < sz and heap[ele_ind] < heap[2 * ele_ind]:
                max_pos = 2 * ele_ind
            if (2 * ele_ind + 1) < sz and heap[max_pos] < heap[2 * ele_ind + 1]:
                max_pos = 2 * ele_ind + 1
            if max_pos == ele_ind:
                break
            heap[ele_ind], heap[max_pos] = heap[max_pos], heap[ele_ind]
            ele_ind = max_pos
    
            
                
    

if __name__ == '__main__':
    data = np.random.randint(0, 100, 10)
    print(data)
    heap = MaxHeap(100, data)
    print(heap.heap)

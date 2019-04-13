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
            self.heapify(self.heap, self.cnt, i)

    def heapify(self, heap, sz, ele_ind):
        while True:
            max_pos = ele_ind
            if (2 * ele_ind <= sz) and heap[ele_ind] < heap[2 * ele_ind]:
                max_pos = 2 * ele_ind
            if (2 * ele_ind + 1) <= sz and heap[max_pos] < heap[2 * ele_ind + 1]:
                max_pos = 2 * ele_ind + 1
            if max_pos == ele_ind:
                break 
            heap[ele_ind], heap[max_pos] = heap[max_pos], heap[ele_ind]
            ele_ind = max_pos

    def remove_max(self):
        if self.cnt == 0 :
            return  - 1
        self.heap[1] = self.heap[self.cnt]
        self.heap[self.cnt] = 0
        self.cnt -= 1
        self.heapify(self.heap, self.cnt, 1)
        return 0
        
    def insert(self, item):
        if self.cnt >= self.sz:
            return False
        self.cnt += 1
        self.heap[self.cnt] = item
        i = self.cnt
        while True:
            if i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2] , self.heap[i]
                i = i // 2
            else:
                return True


                
    

if __name__ == '__main__':
    data = np.random.randint(0, 100, 10)
    print(data)
    heap = MaxHeap(20, data)
    print(heap.heap)
    heap.remove_max()
    print(heap.heap)
    heap.insert(1000)
    print(heap.heap)


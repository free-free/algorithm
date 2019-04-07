# -*- coding:utf-8 -*-


import numpy as np


def merge_sort(a):
    merge_sort_call(a, 0, len(a) - 1)

def merge_sort_call(a, sp, ep):
    if sp >= ep:
        return 
    mp = sp + ((ep - sp) >> 2)
    merge_sort_call(a, sp, mp)
    merge_sort_call(a, mp + 1, ep)
    merge(a, sp, mp, ep)

def merge(a, sp, mp, ep):
    i, j = sp , mp + 1
    tmp = []
    while i <= mp and j <= ep:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    s, e = i, mp
    if j <= ep:
        s, e = j, ep
    while s <= e :
        tmp.append(a[s])
        s += 1
    for i in range(ep - sp + 1):
        a[i + sp] = tmp[i]


def qsort(a):
    qsort_call(a, 0, len(a) - 1)

def qsort_call(a, sp, ep):
    if sp >= ep:
        return 
    pivot = partition(a, sp, ep)
    qsort_call(a, sp, pivot - 1)
    qsort_call(a, pivot + 1, ep)

def partition(a, sp, ep):
    pivot_val = a[ep]
    i = j = sp
    while j < ep:
        if a[j] < pivot_val:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    a[i], a[ep] = a[ep], a[i]
    return i

def bubble_sort(a):
    for i in range(len(a)):
        is_sort = True
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_sort = False
        if is_sort:
            return 

def inserting_sort(a):
    for i in range(len(a)):
        pos = i
        val = a[i]
        for j in range(i, 0, -1):
            if a[j - 1] > val:
                a[j] = a[j - 1]
                pos = j - 1
            else:
                break
        a[pos] = val

def selective_sort(a):
    for i in range(len(a)):
        min_pos = i
        min_val = a[i]
        for j in range(i, len(a)):
            if a[j] < min_val:
                min_val = a[j]
                min_pos = j
        a[i], a[min_pos] = a[min_pos], a[i]
        

if __name__ == '__main__':
    data = np.random.randint(0, 100, 50)
    print(data)
    selective_sort(data)
    print(data)

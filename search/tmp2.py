# -*- coding:utf-8 -*-

import numpy as np


def quick_sort(a):
    quick_sort_call(a, 0, len(a) - 1)

def quick_sort_call(a, sp, ep):
    if sp >= ep:
        return 
    pivot = partition(a, sp, ep)
    quick_sort_call(a, sp, pivot - 1)
    quick_sort_call(a, pivot + 1, ep)

def partition(a, sp, ep):
    i = j = sp
    pivot_val = a[ep]
    while j < ep:
        if a[j] < pivot_val:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    a[ep], a[i] = a[i], a[ep]
    return i

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
    i, j = sp, mp + 1
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
        s, e = j , ep
    while s <= e:
        tmp.append(a[s])
        s += 1
    for i in range(ep - sp + 1):
        a[i + sp] = tmp[i]


def bubble_sort(a):
    for i in range(len(a)):
        is_sort = True
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_sort = False
        if is_sort:
            break

def inserting_sort(a):
    for i in range(1, len(a)):
        val = a[i]
        min_p = i 
        for j in range(i, 0, -1):
            if a[j - 1] > val:
                a[j] = a[j-1]
                min_p = j - 1
            else:
                break
        a[min_p] = val
    
def selective_sort(a):
    for i in range(len(a)):
        min_val = a[i]
        min_p = i
        for j in range(i + 1, len(a)):
            if a[j] < min_val:
                min_val = a[j]
                min_p = j
        a[i], a[min_p] = a[min_p], a[i]


if __name__ == '__main__':
    data = np.random.randint(0, 100, 50)
    print(data)
    selective_sort(data)
    print(data)

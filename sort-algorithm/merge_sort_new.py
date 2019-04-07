# -*- coding:utf-8 -*-


import numpy as np


def merge_sort(a):
    merge_sort_call(a, 0, len(a) - 1)


def merge_sort_call(a, sp, ep):
    if sp >= ep:
        return 
    mp = (sp + ep) // 2
    merge_sort_call(a, sp , mp)
    merge_sort_call(a, mp + 1, ep)
    merge(a, sp, mp, ep)

def merge(a, sp, mp, ep):
    i = sp
    j = mp + 1
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
    while s <= e:
        tmp.append(a[s])
        s += 1
    for i in range(0, ep - sp + 1):
        a[sp + i] = tmp[i]


if __name__ == '__main__':
    data = np.random.randint(0, 50, 50)
    print(data)
    print('*' * 50)
    merge_sort(data)
    print(data)

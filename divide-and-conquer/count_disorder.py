# -*- codin:utf-8 -*-

import numpy as np

def merge_sort_and_disorder(a):
    return merge_sort_call(a, 0, len(a) - 1)

def merge_sort_call(a, sp, ep):
    if sp >= ep:
        return 0
    disorder_cnt = 0
    mp = sp + ((ep - sp) >> 2)
    disorder_cnt += merge_sort_call(a, sp, mp)
    disorder_cnt += merge_sort_call(a, mp + 1, ep)
    disorder_cnt += merge(a, sp, mp , ep)
    return disorder_cnt

def merge(a, sp, mp, ep):
    i , j = sp, mp + 1
    tmp = []
    disorder_cnt = 0
    while i <= mp and j <= ep:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
            disorder_cnt += (mp - i + 1)
    s, e = i, mp
    if j <= ep:
        s, e = j, ep
    while s <= e:
        tmp.append(a[s])
        s += 1
    for i in range(0, ep - sp +1):
        a[sp + i] = tmp[i]
    return disorder_cnt


if __name__ == '__main__':
    data = np.random.randint(0,100, 30)
    data = [3,2,4,3,1,0]
    print(data)
    disorder_cnt = merge_sort_and_disorder(data)
    print(disorder_cnt)
    print(data)

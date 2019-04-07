
import numpy as np


def merge_sort(a):
    merge_sort_c(a, 0, len(a) - 1)


def merge_sort_c(a, s_p, e_p):
    if s_p >= e_p:
        return 
    m_p = (s_p + e_p) // 2
    merge_sort_c(a, s_p, m_p)
    merge_sort_c(a, m_p + 1, e_p)
    merge(a, s_p, m_p, e_p)


def merge(a, s_p, m_p, e_p):
    i = s_p 
    j = m_p + 1
    tmp = []
    while i <= m_p and j <= e_p:
        if (a[i] < a[j]):
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    s, e = i, m_p
    if j <= e_p:
        s, e = j, e_p
    while s <= e:
        tmp.append(a[s])
        s += 1
    for i in range(e_p - s_p + 1):
        a[s_p + i] = tmp[i]

    
if __name__ == '__main__':
    data = np.random.randint(0, 500, 50)
    print(data)
    print('-' * 100)
    merge_sort(data)
    print(data)

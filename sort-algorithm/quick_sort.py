
import numpy as np



def quick_sort(a):
    quick_sort_c(a, 0, len(a) - 1)


def quick_sort_c(a, sp, ep):
    if (sp)>= ep:
        return 
    pivot = partition(a, sp, ep)
    quick_sort_c(a, sp, pivot - 1)
    quick_sort_c(a, pivot, ep)


def partition(a, sp , ep):
    pivot = a[ep] 
    i = j = sp
    while j < ep:
        if a[j] <= pivot:
            tmp = a[i] 
            a[i] = a[j]
            a[j] = tmp
            i += 1
        j += 1
    tmp = a[i]
    a[i] = a[ep]
    a[ep] = tmp
    return i


if __name__ == '__main__':
    data = np.random.randint(0, 500, 50)
    print(data)
    print('-' * 100)
    quick_sort(data)
    print(data)

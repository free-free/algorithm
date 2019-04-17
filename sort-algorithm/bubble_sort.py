

import numpy as np


def bubble_sort(a):
    n = len(a)
    for i in range(n):
        is_sort = True
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_sort = False
        if is_sort:
            break


if __name__ == '__main__':
    data = np.random.randint(0, 100, 50)
    print(data)
    print('*' * 50)
    bubble_sort(data)
    print(data)

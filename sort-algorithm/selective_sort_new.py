
import numpy as np


def selective_sort(a):
    for i in range(0, len(a)):
        min_val = a[i]
        min_pos = i
        for j in range(i, len(a)):
            if a[j] < min_val:
                min_pos = j
                min_val = a[j]
        a[min_pos], a[i] = a[i], a[min_pos]


if __name__ == '__main__':
    data = np.random.randint(0, 100, 50)
    print(data)
    print('*' * 50)
    selective_sort(data)
    print(data)

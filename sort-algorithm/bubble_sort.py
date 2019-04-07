import numpy as np


def bubble_sort(arr):
    is_sorted = True
    for i in range(len(arr)):
        is_sorted = False
        for j in range(len(arr) - i -1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                is_sorted = True
        if not is_sorted:
            break
    return arr



if __name__ == '__main__':
    data = np.random.randint(1, 100, 100)
    print(data)
    print('-'*100)
    print(bubble_sort(data))


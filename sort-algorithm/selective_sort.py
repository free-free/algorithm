import numpy as np



def selective_sort(arr):
    for  i in range(len(arr)):
        min_p = i
        min_val = arr[i]
        for j in range(i + 1, len(arr)):
            if min_val > arr[j]:
                min_p = j
                min_val = arr[j]
        arr[min_p] = arr[i]
        arr[i] = min_val
    return arr


if __name__ == '__main__':
    data = np.random.randint(0, 100, 50)
    print(data)
    print('*' * 100)
    print(selective_sort(data))

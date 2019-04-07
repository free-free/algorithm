import numpy as np

def inserting_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j >= 1:
            tmp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1]  = tmp
            j = j - 1
    return arr
        

def inserting_sort2(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        i_p = i
        for j in range(i, 0, -1):
            if arr[j - 1] > val:
                arr[j] = arr[j - 1]
                i_p = j - 1
            else:
                break
        arr[i_p] = val

    return arr


if __name__ == '__main__':
    data = np.random.randint(1, 100, 50)
    print(data)
    print('*' * 50)
    print(inserting_sort2(data))

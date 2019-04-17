import numpy as np


def inserting_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j - 1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break

if __name__ == '__main__':
    data = np.random.randint(0, 100, 50)
    print(data)
    print('*' * 50)
    inserting_sort(data)
    print(data)

import numpy as np



def quick_sort(a):
    quick_sort_call(a, 0, len(a) - 1)

def quick_sort_call(a, sp, ep):
    if sp >= ep:
        return 
    pivot = partition(a, sp, ep)
    quick_sort_call(a, sp, pivot - 1)
    quick_sort_call(a, pivot + 1, ep)

def partition(a, sp, ep):
    pivot_val = a[ep]
    i = j = sp
    while j <= ep:
        if a[j] < pivot_val:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    a[ep], a[i] = a[i] , a[ep]
    return i

if __name__ == '__main__':
    data = np.random.randint(0, 50, 50)
    print(data)
    print('*' * 50)
    quick_sort(data)
    print(data)

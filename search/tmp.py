
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
    i = j = sp
    pivot_val = a[ep]
    while j < ep:
        if a[j] < pivot_val:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    a[ep], a[i] = a[i], a[ep]
    return i


def merge_sort(a):
    merge_sort_call(a, 0, len(a) - 1)

def merge_sort_call(a, sp, ep):
    if sp >= ep:
        return 
    mp = sp + ((ep - sp) >> 2)
    merge_sort_call(a, sp, mp)
    merge_sort_call(a, mp + 1, ep)
    merge(a, sp, mp, ep)

def merge(a, sp, mp, ep):
    i , j = sp, mp + 1
    tmp = []
    while i <= mp and j <= ep:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    s, e = i, mp
    if j <= ep:
        s, e = j, ep
    while s <= e:
        tmp.append(a[s])
        s += 1
    for i in range(0, ep - sp + 1):
        a[i + sp ] = tmp[i]


def bubble_sort(a):
    for i in  range(0, len(a)):
        is_sort = True
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_sort = False
        if is_sort:
            break

            
def inserting_sort(a):
    for i in range(1, len(a)):
        pi = i
        val = a[i]
        for j in range(i, 0, -1):
            if a[j - 1] > val:
                a[j] = a[j - 1]
                pi = j - 1
            else:
                break
        a[pi] = val

def selective_sort(a):
    for i in range(0, len(a)):
        min_val = a[i]
        min_pos = i
        for j in range(i + 1,len(a)):
            if a[j] < min_val:
                min_val, min_pos = a[j], j
        a[min_pos], a[i] = a[i], a[min_pos]

def find_by_bs(a, val):
    low, mid, high = 0, 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 2)
        if a[mid] < val:
            low = mid + 1
        elif a[mid] > val:
            high = mid - 1
        else:
            return mid
    return -1

def find_first_by_bs(a, val):
    low, mid, high = 0, 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >>2)
        if a[mid] < val:
            low = mid + 1
        elif a[mid] > val:
            high = mid - 1
        else:
            if mid == 0 or a[mid - 1] != val:
                return mid
            high = mid - 1
    return -1

def find_last_by_bs(a, val):
    low, mid, high = 0, 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 2)
        if a[mid] < val:
            low = mid + 1
        elif a[mid] > val:
            high = mid - 1
        else:
            if mid == len(a) - 1 or a[mid + 1] != val:
                return mid
            low = mid + 1
    return -1

def find_first_geq_by_bs(a, val):
    low, mid, high = 0, 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 2)
        if a[mid] >= val:
            if mid == 0 or a[mid - 1] < val:
                return mid
            high = mid -1
        else:
            low = mid + 1
    return -1 

def find_last_leq_by_bs(a, val):
    low, mid, high = 0, 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 2)
        if a[mid] <= val:
            if mid == len(a) - 1 or a[mid + 1] > val:
                return mid 
            low = mid + 1
        else:
            high = mid - 1
    return -1

def find_first_by_binary_search(a, val):
    low, mid, high = 0, 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 2)
        if a[mid] < val:
            low = mid + 1
        elif a[mid] >val:
            high = mid - 1
        else:
            if mid == 0 or a[mid - 1] != val:
                return mid
            high = mid - 1
    return -1

def find_last_by_binary_search(a, val):
    low, mid, high = 0, 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 2)
        if a[mid] < val:
            low = mid + 1
        elif a[mid] > val:
            high = mid - 1
        else:
            if mid == (len(a) - 1) or a[mid + 1] != val:
                return mid
            low = mid + 1
    return -1

def find_first_geq_by_binary_search(a, val):
    low, mid, high = 0, 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 2)
        if a[mid] >= val:
            if mid == 0 or a[mid - 1] < val:
                return mid
            high = mid - 1
        else:
            low = mid + 1
    return -1

def find_last_leq_by_binary_search(a, val):
    low, mid, high = 0, 0, len(a) - 1
    while low <= high:
        mid = low + ((high - low) >> 2)
        if a[mid] <= val:
            if mid == len(a) -1 or a[mid + 1] > val:
                return mid
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    #print(simple_binary_search(data, 10))
    #print(recursive_binary_search(data,0, len(data) - 1,  10))
    #print(find_sqrt_by_binary_search(9999999))
    print('-' * 20 + 'normal test' + '-' * 20)
    data = [1,2, 32, 34, 12, 1, 42, 38, 9, 8, 34, 12 ,34, 19]
    print(data)
    bubble_sort(data)
    print(data)
    print('find 34: ')
    print("The first occurence position: %d" %find_first_by_bs(data, 34))
    print("The last occurence position: %d" %find_last_by_bs(data, 34))
    print("The first larger occurence position: %d" %find_first_geq_by_bs(data, 34))
    print("The last smaller occurence position: %d" %find_last_leq_by_bs(data, 34))
    
    print('find 25: ')
    print("The first occurence position: %d" %find_first_by_bs(data,25 ))
    print("The last occurence position: %d" %find_last_by_bs(data, 25))
    print("The first larger occurence position: %d" %find_first_geq_by_bs(data, 25))
    print("The last smaller occurence position: %d" %find_last_leq_by_bs(data, 25))


    print('find 50: ')
    print("The first occurence position: %d" %find_first_by_bs(data,50 ))
    print("The last occurence position: %d" %find_last_by_bs(data, 50))
    print("The first larger occurence position: %d" %find_first_geq_by_bs(data, 50))
    print("The last smaller occurence position: %d" %find_last_leq_by_bs(data, 50))

    print('-' * 20 + 'boundary test' + '-' * 20)
    print('high boundary test')
    data = [1,2, 32, 34, 12, 1, 12, 20, 9, 8, 34, 12 ,34, 19]
    print(data)
    bubble_sort(data)
    print(data)
    print("The first occurence position: %d" %find_first_by_bs(data, 34))
    print("The last occurence position: %d" %find_last_by_bs(data, 34))
    print("The first larger occurence position: %d" %find_first_geq_by_bs(data, 34))
    print("The last smaller occurence position: %d" %find_last_leq_by_bs(data, 34))
    
    print('low boundary test')
    data = [1,2, 32, 34, 12, 1, 12, 20, 9, 8, 34, 12 ,34, 19]
    print(data)
    bubble_sort(data)
    print(data)
    print("The first occurence position: %d" %find_first_by_bs(data, 1))
    print("The last occurence position: %d" %find_last_by_bs(data, 1))
    print("The first larger occurence position: %d" %find_first_geq_by_bs(data, 1))
    print("The last smaller occurence position: %d" %find_last_leq_by_bs(data,1 ))


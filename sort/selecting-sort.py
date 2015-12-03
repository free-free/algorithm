#!/usr/bin/env python3
def selectingSort(arr):
	mi=0
	num=0
	for i in range(len(arr)):
		mi=i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[mi]:
				mi=j
		num=arr[i]
		arr[i]=arr[mi]
		arr[mi]=num
	return arr

if __name__=='__main__':
	arr=[2,3,4,5,2,43,34,54,3,12,12]
	print('unsort arr',arr)
	print('sorted arr',selectingSort(arr))
		

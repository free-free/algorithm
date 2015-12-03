#!/usr/bin/env python3

def insertSort(arr):
	num=0
	for i in range(1,len(arr)):
		for j in range(i,0,-1):
			if arr[j]<arr[j-1]:
				num=arr[j]
				arr[j]=arr[j-1]
				arr[j-1]=num
			else:
				break
	return arr
if __name__=='__main__':
	s=[21,32,43,465,7,76,5,7623,21,-12,3]
	print('unsort arr',s)
	print('sorted arr',insertSort(s))
				

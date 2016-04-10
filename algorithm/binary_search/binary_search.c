/**********************************************************
*
*@description:binary search algorithm
*@complexity:O(log(N))
*@date:2016/04/10
*
***********************************************************/
#include<stdio.h>
#include <stdlib.h>
#include <time.h>
typedef int ElementType;
#define LENGTH 1000
int binary_search(const ElementType a[],ElementType X,int length)
{
	int start,end,mid;
	start=0;
	end=length-1;
	while(start<=end)
	{
		mid=(end+start)/2;
		if(X>a[mid])
		{
			start=mid+1;
		}
		else if(X<a[mid])
		{
			end=mid-1;
		}
		else
		{
			return mid;
		}
	}
	return -1;
}
ElementType *insertion_sort( ElementType *arr,int length)
{
	int i,j;
	ElementType swap;
	for(i=0;i<length;i++)
	{
		j=i;
		while(j>0&&arr[j]<arr[j-1])
		{	
			swap=arr[j-1];
			arr[j-1]=arr[j];
			arr[j]=swap;
			j--;
		}
	}
	return arr;
}
int main(int argv,char *args[])
{
	ElementType a[LENGTH];
	ElementType *sortedArr=a;
	int pos,i,x;
	srandom((long long unsigned)time(NULL));
	printf("Origin array:\n");
	for(i=0;i<LENGTH;i++)
	{
		a[i]=random()%5000;
		printf("%d ",a[i]);
		if(i==1)
		{
			x=a[i];
		}
	}
	sortedArr=insertion_sort(a,LENGTH);
	printf("\nsorted array\n");
	for(i=0;i<LENGTH;i++)
	{
		printf("%d ",sortedArr[i]);
	}
	pos=binary_search(sortedArr,x,LENGTH);
	if(pos!=-1)
	{
		printf("\nelement %d found in %d\n",x,pos);
	}
	else
	{
		printf("\ncan't find element %d\n",x);
	}
	return 0;
}

#include<stdio.h>
#include<stdlib.h>
/****************************************************************
*
*@description:algorithm one
*@complexity:O(N^3)
*
*
****************************************************************/
int max_subsequece_sum1(const int a[],int n)
{
	int thisSum=0,maxSum=0,i,j,k;
	for(i=0;i<n;i++)
	{
		for(j=i;j<n;j++)
		{
			thisSum=0;
			for(k=i;k<j;k++)
			{
				thisSum+=a[k];
			}
			if(thisSum>maxSum)
			{
				maxSum=thisSum;
			}
		}
	}
	return maxSum;
}
/****************************************************************
*
*@description:algorithm two
*@complexity:O(N^2)
*
***************************************************************/
int max_subsequece_sum2(const int a[],int n)
{
	int thisSum=0,maxSum=0,i,j;	
	for(i=0;i<n;i++)
	{
		thisSum=0;
		for(j=i;j<n;j++)
		{
			thisSum+=a[j];	
			if(thisSum>maxSum)
			{
				maxSum=thisSum;
			}
		}
	}
	return maxSum;
}
/*************************************************************
*
*@description:algorithm three(online algorithm)
*@complexity:O(N)
*
************************************************************/
int max_subsequece_sum3(const int a[],int n)
{
	int maxSum=0,thisSum=0,i=0;
	for(i=0;i<n;i++)
	{
		thisSum+=a[i];
		if(thisSum>maxSum)
		{
			maxSum=thisSum;
		}
		else if(thisSum<0)
		{
			thisSum=0;
		}
	}
	return maxSum;
}
int main(int argv,char * args[])
{
	int a[10]={[0]=1,[1]=-2,[2]=5,[3]=2,-3,9,-4,5,-6,3};
	printf("algorithm one output:%d\n",max_subsequece_sum1(a,10));
	printf("algorithm two output:%d\n",max_subsequece_sum2(a,10));
	printf("algorithm three output:%d\n",max_subsequece_sum3(a,10));
	return 1;
}

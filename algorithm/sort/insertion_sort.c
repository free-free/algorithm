#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int * insertion_sort(int *data,int data_length)
{
	int i,j,swap;
	for(i=0,j=0;i<data_length;i++)
	{			
		j=i;
		while(*(data+j-1)>*(data+j)&&j>0)
		{
			swap=*(data+j-1);
			*(data+j-1)=*(data+j);
			*(data+j)=swap;	
			j--;
		}
	}
	return data;
}

int main(int argv,char *args[])
{
	int a[10],i;
	printf("The origin array:");
	srandom((unsigned long)time(NULL));
	for(i=0;i<10;i++)
	{
		a[i]=random()%1000;
		printf("%d ",a[i]);
	}
	printf("\nThe sorted array:");
	insertion_sort(a,10);
	for(i=0;i<10;i++)
	{
		printf("%d ",a[i]);
	}
	printf("\n");
}

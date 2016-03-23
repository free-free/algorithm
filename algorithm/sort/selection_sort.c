#include<stdio.h>

int * selection_sort(int * data,int data_length)
{
	int i,j,min_index,swap;
	for(i=0;i<data_length;i++)
	{
		min_index=i;
		for(j=i+1;j<data_length;j++)
		{
			if (*(data+j)<*(data+min_index))
			{
				min_index=j;
			}
		}
		if (i!=min_index)
		{
			swap=*(data+i);
			*(data+i)=*(data+min_index);
			*(data+min_index)=swap;
		}
	}
	return data;
}
int main(int argv,char *args[])
{
	int a[10]={32,2,34,5,23,53,89,11,43,54};
	int i=0;
	selection_sort(a,10);
	for(i=0;i<10;i++)
	{	
		printf("%d ",a[i]);
	}
	printf("\n");
	return 0;
}


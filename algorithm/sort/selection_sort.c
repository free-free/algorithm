/*********************************************************
*@description:selection sort algorithm
*@author:HUANGBIAO
*@date:2016/03/24
*@analysis: best:0,worst:n^2
*
**********************************************************/

#include<stdio.h>
#include<stdlib.h>
/* a implementation for type int selection sort algorithm*/
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

typedef struct selection_sort 
{
	int *data;
	int data_length;
	int (*compare_func)(int a,int b);
	int (*exchange_func)(struct selection_sort *s,int i,int j);
}IntSelectionSort;
/*selection sort algorithm for all type data*/
void * selection_sort_for_all_type(IntSelectionSort * obj)
{
	/* the parameter obj is user self defined struct type,
	the struct type must have 'compare_func' and 'exchange_func' function elements and data_length element,
	example like this:
		typedef struct 
		{
			SomeType a[10];
			int (*compare_func)(SomeType a,SomeType b);
			int (*exchange_func)(SomeType *data,int i,int j);
			int data_length;
		}DefineType;
	*/
	int i,j,min_index;
	for(i=0;i<obj->data_length;i++)
	{
		min_index=i;
		for(j=i+1;j<obj->data_length;j++)
		{
			if(obj->compare_func(*(obj->data+j),*(obj->data+min_index))<0)
			{
				min_index=j;
			}
		}
		if (i!=min_index)
		{
			obj->exchange_func(obj,i,min_index);
		}
	}
	return obj->data;
}
int compare_func_for_int(int a,int b)
{
	if(a<b)
	{
		return -1;	
	}
	else if(a>b)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int exchange_func_for_int(IntSelectionSort  *s,int i,int j)
{
	int swap;
	swap=*(s->data+i);
	*(s->data+i)=*(s->data+j);
	*(s->data+j)=swap;
}
IntSelectionSort * init(IntSelectionSort * s,int data_length,void * compare_func,void *exchange_func)
{
	int i;
	s->data=(int*)malloc(sizeof(int)*data_length);
	for(i=0;i<data_length;i++)
	{
		*(s->data+i)=random()%10000;
	}
	s->data_length=data_length;
	s->compare_func=compare_func;
	s->exchange_func=exchange_func;
	return s;
}
int main(int argv,char *args[])
{
	int a[10]={32,2,34,5,23,53,89,11,43,54},i=0;
	IntSelectionSort s,*p;
	p=&s;
	p=init(p,20,compare_func_for_int,exchange_func_for_int);
	selection_sort_for_all_type(p);
	//selection_sort(a,10);
	for(i=0;i<20;i++)
	{	
		printf("%d ",*(p->data+i));
	}
	free(p->data);
	printf("\n");
	return 0;
}


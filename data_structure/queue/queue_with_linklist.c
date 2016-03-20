/**********************************************************************
*
*@description: queue implementation using linklist
*@author:   HUANGBIAO
*@date:     2016/03/20
*@email:    19941222hb@gmail.com
*
**********************************************************************/
#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
	void * next;
	void * data;
}Node;
typedef struct linklist
{
	Node * front;
	Node * rear;
	int nodetype_length;
	int  size;
	void *(*enqueue)(struct linklist *list,void * item);
	void *(*dequeue)(struct linklist *list);
	int  (*is_empty)(struct linklist *list);
}Linklist;

Linklist * queue_init(Linklist *list,void *enqueue,void *dequeue,void * is_empty,int length)
{
	list->front=NULL;
	list->rear=NULL;
	list->nodetype_length=length;
	list->enqueue=enqueue;
	list->dequeue=dequeue;
	list->is_empty=is_empty;
	return list;
}
int is_empty(Linklist *list)
{
	return  list->rear==NULL;
}
void * enqueue(Linklist *list,void * item)
{
	Node *nnode=NULL;
	if (NULL==list->front)
	{
		list->front=(Node*)malloc(sizeof(Node));
		list->front->next=NULL;
		list->front->data=item;
		list->rear=list->front;
	}
	else
	{
		nnode=(Node*)malloc(sizeof(Node));
		nnode->data=item;
		nnode->next=NULL;
		list->front->next=nnode;
		list->front=nnode;	
	}
	return item;
}
void * dequeue(Linklist *list)
{
	void * item=NULL;
	Node * onode=NULL;
	if(list->is_empty(list))
	{	
		return NULL;
	}
	item=list->rear->data;
	onode=list->rear;
	list->rear=list->rear->next;
	free(onode);
	return item;
}

int main(int argv,char *args[])
{
	Linklist *list,l;
	char string[][100]={
		{"Jell is god"},
		{"Jell is shit"},
		{"Jell is bitch"}
	};
	list=&l;
	list=queue_init(list,enqueue,dequeue,is_empty,1);
	list->enqueue(list,string[2]);
	list->enqueue(list,string[1]);
	list->enqueue(list,string[0]);
	while(!list->is_empty(list))
	{	
		printf("%s\n",(char *)list->dequeue(list));
	}
	return 1;
	
}

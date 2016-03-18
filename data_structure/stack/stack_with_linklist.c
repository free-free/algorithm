#include<stdio.h>
#include<stdlib.h>

/********************************************************
*
*@description: a stack implementation using linklist
*@author:  HUANGBIAO
*@date:    2016/3/18
*
*
********************************************************/
typedef struct linknode
{
	int item;
	struct linknode *next;
}Node;

typedef struct stack
{
	Node *first;
	int(*pop)(struct stack *stack);
	int(*push)(struct stack *stack,int item);
	int(*is_empty)(struct stack *stack);
	
}Stack;

Stack* stack_init(Stack * stack,void *pop,void *push,void* is_empty)
{
	stack->first=NULL;
	stack->pop=pop;
	stack->push=push;
	stack->is_empty=is_empty;
	return stack;
}
int push(Stack *stack,int item)
{
	Node *node=(Node*)malloc(sizeof(Node));
	node->item=item;
	node->next=stack->first;
	stack->first=node;
	return item;
}
int pop(Stack *stack)
{
	int item=stack->first->item;
	if (NULL==stack->first)
		return -1;
	stack->first=stack->first->next;
	return item;
}
int is_empty(Stack *stack)
{
	return stack->first==NULL;
}

int main(int argv,char * args[])
{
	Stack *stack;
	Stack s;
	stack=&s;
	stack =stack_init(stack,pop,push,is_empty);
	stack->push(stack,10);
	stack->push(stack,20);
	stack->push(stack,30);
	while (!stack->is_empty(stack))
	{
		printf("pop %d\n",stack->pop(stack));
	}
	return 0;
}

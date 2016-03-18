/*********************************************************************
*@description: a stack implementation using array
*@author:HUANGBIAO
*@email:19941222hb@gmail.com
*@date: 2016/03/18/
*
******************************************************************/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct stack
{
	int   stack_size;
	unsigned int stack_pointer;
	void *stack_data;
	int(*push)(struct stack *stack,int item);
	int(*pop)(struct stack *stack);
	int(*is_empty)(struct stack *stack);
	struct stack*(*resize)(struct stack *stack);
	struct stack*(*shrink)(struct stack *stack);
}Stack;


Stack * stack_init(Stack* stack,int stack_init_length,void *push,void *pop,void *is_empty,void*resize,void*shrink)
{	
	stack->stack_size=stack_init_length;
	stack->stack_pointer=0;
	stack->pop=pop;
	stack->push=push;
	stack->is_empty=is_empty;
	stack->resize=resize;
	stack->shrink=shrink;
	stack->stack_data=(int*)malloc(sizeof(int)*(stack->stack_size));
	return stack;
}
Stack* resize(Stack *stack)
{
	int *data=(int*)malloc(sizeof(int)*2*stack->stack_size);
	memcpy(data,stack->stack_data,sizeof(int)*(stack->stack_size));
	free(stack->stack_data);
	stack->stack_data=(int*)data;
	stack->stack_size=stack->stack_size<<1;
	return stack;
}
Stack * shrink(Stack *stack)
{
	int *data=(int*)malloc(sizeof(int)*(stack->stack_size>>1));
	memcpy(data,stack->stack_data,sizeof(int)*(stack->stack_pointer+1));
	free(stack->stack_data);
	stack->stack_data=data;
	stack->stack_size=stack->stack_size>>1;
	return stack;
}
int is_empty(Stack *stack)
{
	return stack->stack_pointer==0;
}

int push(Stack *stack,int item)
{
	if(stack->stack_pointer>(stack->stack_size-1))
	{
		//resize stack
		stack=stack->resize(stack);
	}
	*((int*)stack->stack_data+stack->stack_pointer)=item;
	stack->stack_pointer++;
	return item;
}

int pop(Stack *stack)
{
	if (stack->is_empty(stack))
	{
		//stack is empty
		return -1;
	}
	//shrink stack data size
	if(stack->stack_pointer<(stack->stack_size>>2))
	{
		stack=stack->shrink(stack);
	}
	stack->stack_pointer--;
	return *((int*)stack->stack_data+stack->stack_pointer);
	
}
int main(int argv,char * args[])
{
	Stack *stack,s;
	stack=&s;
	stack_init(stack,2,push,pop,is_empty,resize,shrink);
	stack->push(stack,10);
	stack->push(stack,20);
	stack->push(stack,30);
	stack->push(stack,40);
	stack->push(stack,50);
	stack->push(stack,60);
	stack->push(stack,70);
	stack->push(stack,80);
	
	while (!stack->is_empty(stack))
	{
		printf("pop %d\n",stack->pop(stack));
	}
	free(stack->stack_data);
	return 0;
}

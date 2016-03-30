/******************************************************
*
*@description:arithmetic expression evaluation
*@author:HUANGBIAO
*@date:2016/03/29
*
******************************************************/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct stack
{
	void *data;
	int length;
	int top;
	int (*is_empty)(struct stack *stack);
	void*(*push)(struct stack *stack,void *item);
	void*(*pop)(struct stack *stack);
}Stack;
Stack *stack_init(Stack *stack,int length,int type_length,void *push,void *pop,void *is_empty)
{
	stack->data=(char*)malloc(type_length*length);
	stack->top=0;
	stack->length=length;
	stack->push=push;
	stack->pop=pop;
	stack->is_empty=is_empty;
}
char* char_stack_push(Stack *stack,char *ch)
{
	if(stack->top==stack->length)
	{
		return NULL;
	}
	*((char*)stack->data+stack->top)=*ch;
	stack->top++;
	return ch;
}

int is_empty(Stack *stack)
{
	return stack->top==0;
}
char *char_stack_pop(Stack *stack)
{
	if (stack->is_empty(stack))
	{
		return NULL;
	}
	stack->top--;
	return &(*((char*)stack->data+stack->top));
}


int * int_stack_push(Stack*stack,int *item)
{
	if(stack->top==stack->length)
	{	
		return NULL;
	}
	*((int*)stack->data+stack->top)=*item;
	stack->top++;
	return item;
}
int * int_stack_pop(Stack*stack)
{
	if (stack->is_empty(stack))
	{
		return NULL;
	}
	stack->top--;
	return &(*((int*)stack->data+stack->top));
}
int main(int argv,char *args[])
{
	Stack *operator,opr,*operand,opd;
	int i,out;
	char ch;
	operator=&opr;
	operand=&opd;
	operand=stack_init(operand,100,1,char_stack_push,char_stack_pop,is_empty);
	operator=stack_init(operator,100,4,int_stack_push,int_stack_pop,is_empty);
	if (argv>=2)
	{
		for(i=0;i<strlen(args[1]);i++)
		{
			switch (args[1][i])
			{
				case '*':
					operand->push(operand,&(args[1][i]));
					break;
				case '+':
					operand->push(operand,&(args[1][i]));
					break;
				case '-':
					operand->push(operand,&(args[1][i]));
					break;
				case '/':
					operand->push(operand,&(args[1][i]));
					break;
				case '%':
					operand->push(operand,&(args[1][i]));
				case '(':
					break;
				case ')':
					ch=*operand->pop(operand);
					if(ch=='*')
					{	
						out=(*operator->pop(operator))*(*operator->pop(operator));
						operator->push(operator,&out);
					}
					else if(ch=='/')
					{	
						out=(*operator->pop(operator))/(*operator->pop(operator));
						operator->push(operator,&out);
					}
					else if(ch=='%')
					{	
						out=(*operator->pop(operator))%(*operator->pop(operator));
						operator->push(operator,&out);
					}else if(ch=='+')
					{
						out=(*operator->pop(operator))+(*operator->pop(operator));
						operator->push(operator,&out);
					}else
					{
						out=(*operator->pop(operator))-(*operator->pop(operator));
						operator->push(operator,&out);
					}						
					
					break;
				default:
					operator->push(operator,&(args[1][i]));
					break;
					
			}
		}
	}
	printf("result:%d\n",*(operator->pop(operator)));
	free(operator->data);
	free(operand->data);
	return 0;
}



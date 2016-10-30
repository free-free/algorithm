/**************************************************************************
*
*@file:min_stack.c
*@author:huangbiao
*@desc:following code implement min stack(that means stack can return minnest value in constant time)
*
*/

#include<stdio.h>
#include<stdlib.h>

struct stack ;
typedef int ElementType;
struct stack{
     ElementType * data;
     int *min_index;
     int size;
     int top;
     int min_top;
     ElementType (*pop)(struct stack * stack);
     ElementType (*push)(struct stack * stack, ElementType item);
     ElementType (*get_min)(void);
};

ElementType push (struct stack * stack , ElementType item);
ElementType pop(struct stack *stack);
ElementType get_min(struct stack * stack);

struct stack *
stack_init(struct stack *stack,
           int length,
           void * push,
           void * pop,
           void * get_min)
{
	stack = (struct stack *)malloc(sizeof(struct stack));
        stack->data = (ElementType*)malloc(sizeof(ElementType)*length);
        if (NULL == stack->data)
            return NULL;
        stack->min_index= (ElementType*)malloc(sizeof(int)*length);
        if (NULL == stack->min_index)
            return NULL;
        stack->top = -1;
        stack->min_top = -1;
        stack->pop = pop;
        stack->size = length;
        stack->push  = push;
        stack->get_min = get_min;
        return stack;
} 

ElementType push (struct stack * stack , ElementType item)
{
	stack->top++;
        if(stack->top > stack->size-1)
        {
            return ;
        }
        if(stack->min_top == -1)
        {
		stack->min_index[++stack->min_top] = stack->top;
	}
        if (item < stack->data[stack->min_index[stack->min_top]])
        {
		stack->min_top++;
                stack->min_index[stack->min_top] = stack->top;
	}
        stack->data[stack->top] = item;
        return item;
}

ElementType 
pop(struct stack *stack)
{
        ElementType item;
        if (stack->top == -1)
        {
            return ;
	}
        item = stack->data[stack->top--];
        if(item == stack->data[stack->min_index[stack->min_top]])
	{
            stack->min_top--;
	}
        return item;
}

ElementType 
get_min(struct stack *stack)
{
	return stack->data[stack->min_index[stack->min_top]];
}

/* not fully testing  code */
int 
main(int argc, char* argv[])
{
	struct stack *stack = NULL;
        stack = stack_init(stack, 20, push, pop, get_min);
        stack->push(stack, 20);
        stack->push(stack, 10);
        stack->push(stack, 30);
        stack->push(stack, 5);
        stack->push(stack, 40); 
        printf("min item %d\n", stack->get_min());
        stack->pop(stack);	
        stack->pop(stack);	
        printf("min item %d\n", stack->get_min());
}

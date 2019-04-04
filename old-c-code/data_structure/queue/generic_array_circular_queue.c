#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


typedef struct
{
	uint32_t i;
	uint32_t j;
	uint32_t k;
	uint32_t z;	
}dt;

// generic array circular queue data structure
typedef struct
{
	dt * xData;
	uint32_t ulRear;
	uint32_t ulFront;
	uint32_t ulMaxSize;
}ga_cqueue_t;


#define gacq_Create(pxQueue, maxSize) ({\
	pxQueue = NULL;\
	pxQueue = (typeof(pxQueue))malloc(sizeof(typeof(*pxQueue)));\
	if(pxQueue != NULL)\
	{\
		pxQueue->xData = NULL;\
		pxQueue->xData = (typeof(pxQueue->xData))malloc(sizeof(typeof(*(pxQueue->xData)))*maxSize);\
		printf("total byte size:%ld\n",sizeof(typeof(*(pxQueue->xData)))*maxSize);\
		if(pxQueue->xData != NULL) \
		{\
			pxQueue->ulRear = 0;\
			pxQueue->ulFront = 0;\
			pxQueue->ulMaxSize = maxSize;\
		}\
		else \
		{\
			free(pxQueue);\
			pxQueue = NULL;\
		}\
	}\
})


#define gacq_IsEmpty(pxQueue)({\
	pxQueue->ulFront == pxQueue->ulRear;\
})


#define gacq_Dequeue(pxQueue)({\
	typeof(*(pxQueue->xData)) _item;\
	if(pxQueue->ulFront != pxQueue->ulRear)\
	{\
		_item = pxQueue->xData[pxQueue->ulRear];\
		pxQueue->ulRear = (pxQueue->ulRear + 1) % pxQueue->ulMaxSize;\
	}\
	_item = _item;\
})


#define gacq_Enqueue(pxQueue, item)({\
	if((pxQueue->ulFront + 1)%pxQueue->ulMaxSize == pxQueue->ulRear)\
	{\
		gacq_Dequeue(pxQueue);\
	}\
	pxQueue->xData[pxQueue->ulFront] = item;\
	pxQueue->ulFront = (pxQueue->ulFront + 1) % pxQueue->ulMaxSize;\
})


int main(int argc, char * argv[])
{
	uint32_t i = 0;
	ga_cqueue_t * queue = NULL;
	dt data={0,0,0,0};
	printf("before allocation: %p\n", queue);
	gacq_Create(queue,6);
	printf("after allocation:%p\n", queue);
	gacq_Enqueue(queue, data);
	data.i = 1;
	gacq_Enqueue(queue, data);
	data.i = 2;
	gacq_Enqueue(queue, data);
	data.i = 3;
	gacq_Enqueue(queue, data);
	data.i = 4;
	gacq_Enqueue(queue, data);
	data.i = 5;
	gacq_Enqueue(queue, data);
	data.i = 6;
	printf("queue maximum size:%d\n", queue->ulMaxSize);
	printf("queue's front: %d\n", queue->ulFront);
	printf("queue's rear: %d\n", queue->ulRear);
	while(!gacq_IsEmpty(queue))
	{
		printf("queue's %dth element = %d\n", i++, gacq_Dequeue(queue).i);
	}
	/*
	printf("queue's first item: %d\n", gacq_Dequeue(queue).i);
	printf("queue's rear: %d\n", queue->ulRear);
	printf("queue's second item: %d\n", gacq_Dequeue(queue).i);
	printf("queue's rear: %d\n", queue->ulRear);
	printf("queue's third item: %d\n", gacq_Dequeue(queue).i);
	printf("queue's rear: %d\n", queue->ulRear);
	*/
	return 0;
}



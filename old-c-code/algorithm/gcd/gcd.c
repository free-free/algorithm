/********************************************************
*@description:gcd algorithm
*@complexity:O(log(N))
*
*
********************************************************/
#include<stdio.h>
typedef int ElementType;

ElementType gcd(ElementType m,ElementType n)
{
	ElementType rem,greater_num,smaller_num;
	greater_num=m>n?m:n;
	smaller_num=m<n?m:n;
	while(smaller_num>0)
	{
		rem=greater_num%smaller_num;
		greater_num=smaller_num;
		smaller_num=rem;
	}
	return greater_num;
}

int main(int argv,char * args[])
{
	ElementType m,n;
	m=50;
	n=15;
	printf("max common divider %d\n",gcd(m,n));
	return 0;
}


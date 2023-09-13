/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section

Boundary Condition(s): 
	3 < N < 100

Input Format:
	The first line contains N.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		5
Output
	1*3*5
	-7*9
	--11

Example Input/Output 2:
	Input
		8
	Output 
		2*4*6*8
		-10*12*14
		--16*18 
		---20
*/


#include<stdio.h> 
#include<stdlib.h>

int main()
{
	int n,k,t,1=0; 
	scanf("%d",&n); 
	int g;
	if(n%2==0)
	{
		k=t=2; 
		while(t<=n)
		{
			l++; 
			t+=2;
		}
		g=1;
		for(int i=0;i<g;i++)
		{
			for (int j=0;j<i;j++)
				printf("-");
			for (int f=0;f<l;f++)
			{
				if(f<l-1) 
					printf("%d*",k);
				else 
					printf("%d",k);
					k+-2;
			}	
			printf("\n");
		}
	}
	else
	{
		k=t=1;
		while(t<=n)
		{
			t+=2;
			l++;
		}
		g=l;
		for (int i=0;i<g;i++)
		{
			for (int j=0;j<i;j++)
				printf("-");
			for (int f=0;f<1;f++)
			{
				if(f<l-1) 
					printf("%d*",k); 
				else
					printf("%d",k); 
				k+=2;
			}
			printf("\n");
		}
	}
}
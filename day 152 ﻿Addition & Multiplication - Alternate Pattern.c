/*

The program must accept an integer N as the input. Theprogram must312421104057@stjosephstech731+96=print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	1 <= N <= 20

Input Format:
	The first line contains N.

Output Format:
	The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		5
	Output:
		1+2+3+4+5=15
		1*2*3*4=24
		1+2+3=6
		1*2=2
		1=1

Example Input/Output 2:
	Input:
		8
	Output:
		1+2+3+4+5+6+7+8=36
		1*2*3*4*5*6*7=5040
		1+2+3+4+5+6=21
		1*2*3*4*5=120
		1+2+3+4=10
		1*2*3=6
		1+2=3
		1=1

*/



#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d", &n);
	int s=0;
	for(int i=1;i<=n;i++)
	{
		if(i%2!=0)
			s=0;
		else
			s=1;
		for(int j=1;j<=n-i+1;j++)
		{
			if(i%2!=0)
			{
				s+=j;
				printf("%d",j); 
				if(j<n-i+1)
					printf("+");
			}
			else
			{
				s*=j;
				printf("%d",j); 
				if(j<n-i+1) 								printf("*");
			}
		}
		printf("=%d\n",s);
		}
	}
}
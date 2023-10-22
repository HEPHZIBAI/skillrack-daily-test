/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	2 <= N <= 50

Input Format:
	The first line contains N.

Output Format:
	The N lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		5
	Output
		1 5 2 4 3 3 4 2 5 1
		* 1 4 2 3 3 2 4 1 *
		* * 1 3 2 2 3 1 * *
		* * * 1 2 2 1 * * *
		* * * * 1 1 * * * *

Example Input/Output 2:
	Input:
		4
	Output:
		1 4 2 3 3 2 4 1
		* 1 3 2 2 3 1 *
		* * 1 2 2 1 * *
		* * * 1 1 * * *
*/
#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n
	scanf("%d", &n);
	for (int i=0;i<n;i++)
	{
		for(int j=0;j<i;j++)
		{
			printf("*");
		}
		for (int h=n-i,k=1;h>=1&&k<=n-i;h--,k++)
		{ 
			printf("%d %d ",k,h);
		}
		for (int j=0;j<i;j++)
		{
			printf("*");
		}
		printf("\n");
	}
}
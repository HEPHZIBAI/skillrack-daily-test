
/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	3 <= N <= 1000

Input Format:
	The first line contains N.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input: 
		7
	Output:
		1
		2 3
		4 5 6 7

Example Input/Output 2:
	Input:
		31
	Output:
		1
		2 3
		4 5 6 7
		8 9 10 11 12 13 14 15
		16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31

Example Input/Output 3:
	Input:
		20
	Output:
		1
		2 3
		4 5 6 7
		8 9 10 11 12 13 14 15
		16 17 18 19 20 * * * * * * * * * * *
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n);
	int a=1;
	int k=1;

	for(int i=0;i<n;i++)
	{
		for(int j=1;j<=k;j++)
		{
			if(a>n)
				printf("*");
			else
				printf("%d,a++);
		}
		k+=k;
		printf("\n");
		if(a>n)
			break;
	}
}

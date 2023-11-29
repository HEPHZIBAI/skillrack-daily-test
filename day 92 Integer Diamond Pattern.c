/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	3 <= N <= 50

Input Format:
	The first line contains N.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
		4
	Output
		* * * 1 * * *
		* * 2 1 2 * *
		* 3 2 1 2 3 *
		4 3 2 1 2 3 4
		* 3 2 1 2 3 *
		* * 2 1 2 3 *
		* * * 1 * * *

Example Input/Output 2:
	Input:
		5
	Output:
		* * * * 1 * * * *
		* * * 2 1 2 * * *
		* * 3 2 1 2 3 * *
		* 4 3 2 1 2 3 4 *
		5 4 3 2 1 2 3 4 5
		* 4 3 2 1 2 3 4 *
		* * 3 2 1 2 3 * *
		* * * 2 1 2 * * *
		* * * * 1 * * * *
*/
include<stdio.h>
#include<stdlib.h>

int main()
{
	int n; 
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n-i-1;j++)
			printf("* ");
	
		for(int j=k;j>0;j--) 
			printf("%d ",j);

		for(int j=2;j<=k;j++) 
			printf("%d ",j);
		
		for(int j=0;j<n-i-1;j++)
			printf("* ");

		printf("\n"); 
		k+=1;
	} 
	k=n-1;
	for(int i=0;i<n-1;i++)
	{
		for(int j=0;j<=i;j++) 
			printf("* ");

		for(int j=k;j>0;j--) 
			printf("%d ",j);

		for(int j=2;j<=k;j++) 
			printf("%d ",j);

		for(int j=0;j<=i;j++) 
			printf("* ");
	
		k--; 
		printf("\n");
	}
}

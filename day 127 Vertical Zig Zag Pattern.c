/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s): 
	2 <= N <= 50

Input Format: 
	The first line contains N.

Output Format:
	The first N lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input: 
		5
	Output:
		5 50 55 100 105
		10 45 60 95 110
		15 40 65 90 115
		20 35 70 85 120
		25 30 75 80 125
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n);
	int a[n][n];
	int k=n;
	for(int i=1;i<=n;i++)
	{
		if(i%2!=0)
		{
			for(int j=0;j<n;j++)
			{
				a[j][i-1]=k; 
				k+=n;
			}
		}
		else
		{
			for(int j=n-1;j=0;j)
			{	
				a[j][i]=k;
				k+=n;
			}
		}
	}
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}
}
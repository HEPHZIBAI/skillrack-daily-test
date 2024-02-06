/*
The program must accept the size of two grids(RxC and MxN) as the input. The program must print the MxN grid of RxC grids of asterisks as shown in the Example Input/Output section.

Boundary Condition(s):
	2 <= R, C, M, N <= 20

Input Format:
	The first line contains R and C separated by a space.
	The second line contains M and N separated by a space.

Output Format:
	The lines containing the MxN grid of RxC grids of asterisks as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		2 3
		4 4
	Output:
	
		***|***|***|***
		***|***|***|***
		---+---+---+---
		***|***|***|***
		***|***|***|***
		---+---+---+---
		***|***|***|***
		***|***|***|***
		---+---+---+---
		***|***|***|***
		***|***|***|***

Example Input/Output 2:
	Input:
		3 3
		3 2
	Output:
		***|***
		***|***
		***|***
		---+---
		***|***
		***|***
		***|***
		---+---
		***|***
		***|***
		***|***
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int r,c,m,n;
	scanf("%d %d\n%d %d",&r,&c,&m,&n); 
	for (int w=0;w<m;w++)
	{
		for(int i=0;i<r;i++)
		{
			for(int k=0;k<n;k++)
			{
				for(int j=0;j<c;j++)
				{
					printf("*");
				}
				if(k! =n-1)
					printf("|");
			}
			printf("\n");
		}
		if(w!=m-1)
		{
			for(int j=0;j<n;j++)
			{
				for(int i=0;i<c;i++)
				{
					printf("-");
				}
				if(j!=n-1)
					printf("+");
			}
			printf("\n");
		}
	}
}
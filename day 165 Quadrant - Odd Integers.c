/*
The program must accept an integer matrix of size RxC as the input. The program must print the quadrant of the matrix which contains the maximum number of odd integers as the output. If more than one quadrants have the same maximum number of odd integers, the
program must print -1 as the output.

Note: R and C must be even. At least one odd integer is always present in the matrix.

Boundary Condition(s):
	2 <= R, C <= 50

Input Format:
	The first line contains R and C separated by a space.
	The next R lines, each containing C integers separated by a space.

Output Format:
	The lines containing the quadrant of the matrix which contains the maximum number of odd integers or -1.

Example Input/Output 1:
	Input:
		6 6
		40 18 35 39 42 28
		22 46 30 44 27 17
		35 47 45 40 12 17
		45 23 59 47 47 33
		35 31 44 27 12 39 
		21 32 33 42 23 18
	Output:
		45 23 59
		35 31 44
		21 32 33
	Explanation:
		The quadrant of the matrix which contains the maximum number of odd integers is highlighted below.
		40 18 35 39 42 28
		22 46 30 44 27 17
		35 47 45 40 12 17
		45 23 59 47 47 33
		35 31 44 27 12 39 
		21 32 33 42 23 18

Example Input/Output 2: 
	Input:
﻿		2 4
		22 18 28 17
		30 34 39 40
	Output: 
		-1
*/


#include<stdio.h>
#include<stdlib.h>

int main()
{
	int r,c;
	scanf("%d%d",&r,&c);
	int a[r][c],w[5];
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	int s=0,l=0,f=0;
	
	for(int i=0;i<r/2;i++)
	{
		for(int j=0;j<c/2;j++)
		{
			if(a[i][j]%2!=0)
			{
				s+=1;
			}
		}
	}

	if(l<s)
	{
		l=s;
		f=1;
	}

	w[0]=s;
	s=0;
	
	for(int i=0;i<r/2;i++)
	{
		for(int j=c/2;j<c;j++)
		{
			if(a[i][j]%2!=0)
				s+=1;
		}
	}

	if(l<s)
	{
		l=s;
		f=2;
	}
	w[1]=s;
	s=0;
	for(int i=r/2;i<r;i++)
	{
		for(int j=0;j<c/2;j++)
		{
			if(a[i][j]%2!=0)
				s+=1;
		}
	}
	if(l<s)
	{
		l=s;
		f=3;
	}
	w[2]=s;
	s=0;
	for(int i=r/2;i<r;i++)
	{
		for (int j=c/2;j<c;j++)
		{
			if(a[i][j]%2!=0) 
				s+=1;
		}
	}
	if(l<s)
	{
		l=s;
		f=4;
	}
	w[3]=s;
	int cc=0;
	
	for(int i=0;i<5;i++)
	{
		if(w[i]==l)
			cc+=1;
	}
	if(cc>1)
	{
		printf(-1);
		return 0;
	}
	switch(f)
	{
		case 1:
		{
			for(int i=0;i<r/2;i++)
			{
				for(int j=0;j<c/2;j++)
				{
					printf("%d ",a[i][j]);
				}
				printf("\n");
			}
		}
		break;
		
		case 2:
		{
			for(int i=0;i<r/2;i++)
			{
				for(int j=c/2;j<c;j++)
				{
					printf("%d ",a[i][j]);
				}
				printf("\n");
			}
		}
		break;

		case 3:
		{
			for(int i=r/2;i<r;i++)
			{
				for(int j=0;j<c/2;j++)
				{
					printf("%d ",a[i][j]);
				}
				printf("\n");
			}
		}
		break;

		case 4:
		{
			for(int i=r/2;i<r;i++)
			{
				for(int j=c/2;j<c;j++)
				{
					printf("%d ",a[i][j]);
				}
				printf("\n");
			}
		}
	}
	printf("%d",1);
}



﻿
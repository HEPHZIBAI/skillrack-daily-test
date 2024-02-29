/*
The program must accept an integer matrix of size RxC as the input. If any cell is 0 in the matrix, the program must replace the entire row and column of the cell with zero. Finally, the program must print the modified matrix as the output.

Boundary Conditon(s):
	2 <= R, C <= 50
	0 <= Each integer value <= 1000

Input Format:
	The first line contains R and C separated by a space.
	The next R lines, each containing C integers separated by a space.

Output Format:
	The first R lines. each containing C integers separated by a
space.

Example Input/Output 1:
	Input:
		2 3
		1 0 1
		1 1 1
	Output:
		0 0 0 
		1 0 1
	Explanation:
		In the given 2x3 matrix, the 0 is present in the first row and second column.
		So the entire first row and the entire second column are replaced with zero. Now, the matrix becomes
		0 0 0 
		1 0 1

Example Input/Output 2:
	Input:
		3 4
		3 8 3 8
		0 5 7 8	
		6 0 4 8
	Output:
		0 0 3 8
		0 0 0 0 
		0 0 0 0
*/


#include<stdio.h>
#include<stdlib.h>

int call(int i,int j,int r,int c,int b[r][c])
{
	for (int x=0;x<c;x++)
	{
		b[i][x]=0;
	}
	for(int y=0;y<r;y++)
	{
		b[y][j]=0;
	}
}

int main()
{
	int r,c;
	scanf("%d %d",&r,&c); 
	int a[r][c],b[r][c]; 
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			scanf("%d",&a[i][j]); 
			b[i][j]=a[i][j];
		}
	}

	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(a[i][j]==0)
				call(i,j,r,c,b);
		}
	}

	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			printf("%d ",b[i][j]);
		}
		printf("\n");
	}
}

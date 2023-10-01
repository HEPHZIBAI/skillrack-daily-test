/*
The program must accept an integer matrix of size RxC as the input. The program must print YES if all the integers in the border of the matrix are even. Else the program must print NO as the output.

Boundary Condition(s): 
	2<=R,C<=100

Input Format:
	The first line contains R and C.
	The next R lines each contain C integers separated by a space.

Output Format:
	The first line contains YES or NO.

Example Input/Output 1:
	Input 
		3 4
		86 76 78 10
		84 21 83 38
		44 10 94 36
	Output
		YES
	Explanation:
		In the 3x4 matrix, all the integers in the border of the matrix are even. 86 76 78 10 84 21 83 38 44 10 94 36
		Hence the output is YES

*/

#include<stdio.h> 
#include<stdlib.h>

int main()
{	
	int r,c; 
	scanf("%d %d", &r,&c); 
	int a[r][c]; 
	int m=1; 
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<c;j++)
		{
			scanf("%d",&a[i][j]); 
			if(i==0|| i==r-1||j==0 j==c-1)
			{
				if(a[i][j]%2!=0)
					m=0;
			}
		}
	}
	printf( m==1?"YES" : "NO");
}
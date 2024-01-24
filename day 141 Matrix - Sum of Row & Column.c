/*
The program must accept an integer matrix of size NxN and an integer X as the input. The program must print the sum of the integers in the Xth row and the sum of the integers in the Xth column of the matrix as the output.

Boundary Condition(s):
	2 <= N <= 50
	1 <= X <= N

Input Format:
	The first line contains N.
	The next N lines each contain N integers separated by a space.
	The (N+2)nd line contains X.

Output Format:
	The first line contains the two integers separated by a space as per the given condition.

Example Input/Output 1:
	Input:
		3
		1 2 3
		4 5 6
		7 8 9
		2
	Output:
		15 15
	Explanation:
		Here X = 2.
		In the given 3x3 matrix, the integers in the 2nd row and the 2nd column are highlighted below.
		1 2 3
		4 5 6
		7 8 9
		The sum of the integers in the 2nd row is 15 (4+5+6).
		The sum of the integers in the 2nd column is 15 (2+5+8).
		Hence the output is 15 15


Example Input/Output 2: 
	Input:
		4
		12 45 13 28
		93 58 26 80
		27 22 10 12
		74 89 32 28
		3
	Output: 
		71 81

*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d", &n); 
	int a[n][n],×;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{	
			scanf("%d",&aa[i][j]);
		}
	}
	scanf("%d",&x);
	int s=0,r=0;
	X--;
	for(int i=0;i<n;i++)
	{
		s+=a[x][i];
		r+=a[i][x];
	}
	printf("%d %d",s,r);
}
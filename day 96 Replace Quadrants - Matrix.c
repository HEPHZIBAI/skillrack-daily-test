/*
The program must accept an integer matrix of size NxN as the input. The program must modify the matrix based on the following conditions in the given order.
- The top-right quadrant of the matrix is replaced by the bottom-left quadrant. 
- The bottom-right quadrant of the matrix is replaced by the top-left quadrant. 
Finally, the program must print the modified matrix as the output.
Note: The value of N is always even.

Boundary Condition(s):
	2 <= N <= 50

Input Format:
	The first line contains N.
	The next N lines each contain N integers separated by a space.

Output Format:
	The first N lines each contain N integers of the modified matrix separated by a space.

Example Input/Output 1:
	Input
		4
		25 28 84 71
		68 51 56 70
		17 19 79 29
		87 90 52 75
	Output:
		25 28 17 19
		68 51 87 90
		17 19 25 28
		87 90 68 51
	Explanation:
		The top-right and bottom-loft quadrant of the matrix are highlighted below.
		25 28 84 71
		68 51 56 70
		17 19 79 29
		87 90 52 75
		The bottom-right and quadrant of the matrix are highlighted below.
		25 28 84 71
		68 51 56 70
		17 19 79 29
		87 90 52 75
		After replacing the quadrants as per the given conditions, the matrix becomes
		25 28 17 19
		68 51 87 90
		17 19 25 28
		87 90 68 51

Example Input/Output 2:
	Input:
		6
		65 35 64 63 88 85
		45 14 17 54 45 33
		46 58 32 35 76 54
		88 71 39 92 20 86
		71 66 96 34 96 57
		59 10 46 62 22 22

Output:
		65 35 64 88 71 39
		45 14 17 71 66 96
		46 58 32 59 10 46
		88 71 39 65 35 64
		71 66 96 45 14 17
		59 10 46 46 58 32
*/

#include<stdio.h> 
#include<stdlib.h>

int main() 
{
	int n;
	scanf("%d",&n); 
	int a[n][n];
	for(int i=0;i<n;i++)
	{ 
		for(int j=0;j<n;j++)
		{ 
			scanf("%d",&a[i][j]);
		}
	}
	int k=n/2;
	for(int i=k;i<n;i++)
	{ 
		for(int j=k;j<n;j++)
		{
			a[i][j]=a[i-k][j-k];
		} 
	}
	for(int i=0;i<k;i++)
	{ 
		for(int j=k;j<n;j++) 
		{ 
			a[i][j]=a[i+k][j-k];
		} 
	}
	for(int i=0;i<n;i++) 
	{
		for(int j=0;j<n;j++)
		{
			printf("%d",a[i][j]);
		}
		printf("\n");
	}
}
/*
The program must accept an integer matrix of size NxN and an integer X as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Note: The integer X occurred only once in the given matrix.

Boundary Condition(s): 
	2 <= N <= 50

Input Format:
	The first line contains N and X separated by a space. The next N lines each contain N integers separated by a space.

Output Format:
	The first four lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		4 11
		1 5 6 9
		8 11 4 10
		13 14 20 28
		67 82 14 21
	Output:
		11 5 6 9
		11 4 10 28 21
		11 14 82 67
		11 8 1
	Explanation:
		Here X 11, so the center point the swastik pattern is 11. The integers in the swastik pattern are highlighted below.
		1 5 6 9
		8 11 4 10
		13 14 20 28
		67 82 14 21

Example Input/Output 2:
	Input
		6 69
		21 51 87 14 97 27
		92 96 60 19 55 17
		74 11 16 69 90 54
		30 98 93 67 46 76
 		38 75 86 34 20 91	
		29 89 23 47 95 72
	Output:
		69 19 14 97 27
		69 90 54 76 91 72
		69 67 34 47 23 89 29
		69 16 11 74 92 21
	Explanation:
		Here X = 69, so the center point the swastik pattern is 69. The integers in the swastik pattern are highlighted below.
		21 51 87 14 97 27
		92 96 60 19 55 17
		74 11 16 69 90 54
		30 98 93 67 46 76
 		38 75 86 34 20 91	
		29 89 23 47 95 72

Example Input/Output 3:
	Input:
		3 3
		1 2 3
		4 5 6
		7 8 9
	Output:
		3
		3
		3 6 9 8 7
		3 2 1
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n,x,p=-1,q=-1;
	scanf("%d %d",&n,&x);
	int a[n][n];
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
			if(a[i][j]=x && q=-1)
			{
				p=i;
				q=j;
			}
		}
	}
	
	for(int i=p;i>=0;i--) 
		printf("%d ",a[i][q]);
	
	if(p!=0)
		for(int i=q+1;i<n;i++) 
			printf("%d",a[0][i]);
	printf("\n");

	for(int i=q;i<n;i++)
		printf("%d ",a[p][i]);
	
	if(q!=n-1)
		for(int i=p+1;i<n;i++) 
			printf("%d",a[1][n-1]);
	printf("\n");

	for(int i=p;i<n;i++)
		printf("%d",a[i][q]);

	if(p!=n-1)
		for (int i=q-1;i>=0;i--)
			printf("%d",a[n-1][i]);
	printf("\n");

	for (int i=q;i>=0;i--)
		printf("%d",a[p][i]);

	if(q!=0)
		for(int i=p-1;i>=0;i--) 
			printf("%d ",a[i][0]);
}
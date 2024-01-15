/*

The program must accept an integer matrix of size RxC and four integers X1, Y1, X2 and Y2 as the input. X1, Y1, X2 and Y2 represent the indices of the top-left integer and bottom-right integer of a submatrix. The program must print the submatrix that can be formed using the given indices and the sum of the integers in the submatrix as the output. If it is not possible to form such a submatrix, the program must print -1 as the output

Note: The index of the top-left integer in the given RxC matrix is always (0.0.

Boundary Condition(s): 
	2 <= RC <= 100 
	-1000 <= Matrix element value <= 1000 
	0<=X1, Y1, X2, Y2 <= 100

Input Format:
	The first line contains R and C separated by a space. 
	The next R. lines, each containing C integers separated by a space. 
	The (R+2ynd line contains X1, Y1, X2 and Y2 separated by a space.

Output Format:
	The lines contain the integer value(s) based on the given conditions.

Example Input/Output 1:
	Input:
		4 5
		1 2 3 4 6
		5 3 8 1 2
		4 6 7 5 5
		2 4 8 9 4
		2 0 3 4
	Output:
		4 6 7 5 5
		2 4 8 9 4
		54
	Explanation:
		The index of the top-left integer in the submatrix is (2, 0). 
		The index of the bottom-right integer in the submatrix is (3, 4). 
		So the integers in the submatrix are 4, 6, 7, 5, 5, 2, 4, 8, 9 and 4. 
		The sum of integers in the submatrix is 54.

Example Input/Output 2:
	Input
		4 3
		1 6 8
		8 9 7
		4 6 6
		0 0 2
		1 1 2 3
	Output:
		-1
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int r,c,x,y,z,t,s=0; 
	scanf("%d%d",&r,&c);
	int a[r][c];
	for(int i=0;i<n;i++) 
	{
		for(int j=0;j<c;j++)
		{ 
			scanf("%d",&a[i][j]);
		}
	} 
	scanf("%d%d%d%d",&x,&y,&z,&t); 
	
	if(!(x<r && y<c && z<r && t<c))
		printf("-1\n");

	else
	{
		for(int i=x;i<=z && i<n;i++)
		{
			for(int j=y;j<t && j<c;j++)
			{
				printf("%d",a[1][1]);
				s+a[i][j];
			}
		printf("\n");
		}
		printf("%d",s);	
	}
}
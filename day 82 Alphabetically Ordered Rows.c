/*
The program must accept a character matrix of size RxC containing only lower case alphabets as the input. The program must print the count of rows in the matrix where the alphabets are sorted in alphabetical order as the output.

Boundary Condition(s):
	2 <= R C <= 50

Input Format:
	The first line contains R and C separated by a space. The next R lines each contain C characters separated by a space.

Output Format:
	The first line contains the count of rows in the matrix where the alphabets are sorted in alphabetical order.

Example Input/Output 1:
	Input
		5 4
		a s d f
  		h i j k
		z x y q
		r s t u
		u t x k
	Output
		2
	Explanation:
	In 5x4 matrix, the alphabets in the second row and the fourth row are sorted in alphabetical order.
	Second row: hijk
	Fourth row. rstu
	Hence the output is 2

Example Input/Output 2:
	Input
		3 3
		i j o
 		a z b
		p c e
	Output:
		1
*/
#include<stdio.h> 
#include<stdlib.h>

int main()
{
	int r,c;
	scanf("%d %d\n",&r,&c);
	char a[r][c];
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++) 
		{
			scanf("%c",&a[i][j]);
		}
		scanf("\n");
	}
	int s=0;
	int t=0;
	for(int i=0;i<r;i++)
	{
		t=0;
		for(int j=0;j<c-1;j++)
		{
			if(a[i][j]>a[i][j+1])
			{
				break;
			}
			t++;
		}
		if(t==c-1)	
		{
			s+=1;
		}
	}
	printf("%d",s);
}
/*
The program must accept a character matrix of size NxN containing only alphabets as the input. The program must replace the innermost layer and the outermost layer of the matrix by the asterisk. Then the program must print the modified matrix as the output

Boundary Condition(s): 
	3 <= N <= 100

Input Format:
	The first line contains N. The next N lines each contain N alphabets separated by a space.

Output Format:
	The first N lines containing the modified matrix.

Example Input/Output 1:
	Input
		5
		d z y w y
		y k h a j
		z y b w l
		w i n t w
		e r t y u
	Output:
		* * * * *
		* k h a *
		* y * w *
		* i n t *
		* * * * *
	Explanation:
		In the given 5x5 matrix, the innermost layer and the outermost layer are highlighted below.
		dzywy
		ykhaj 
		zybwl
		wintw
		ertyu
After replacing the innermost layer and the outermost layer of the matrix by the asterisk, it becomes
		*****
		*kha*
		*y*w*
		*int*
		*****

Example Input/Output 2:
	Input
		8
		UALKYANV
		SIUGDTAZ
		DTBJPDCA
		UZSTQHOC
		AQCURMMC
		DRATBOTJ
		XXSRDTPM
		FZFEOCGA
	Output:
		* * * * * * * * 
		* I U G D T A *
		* T B J P D C *
		* Z S * * H O *
		* Q C * * M M *
		* R A T B O T *
		* X S R D T P *
		* * * * * * * *

Example Input/Output 3:
	Input:
		4
		h x b l
		u q i v
		y c y o
		e m a c
	Output:
		* * * *
		* * * *
		* * * *
		* * * *
		
*/

include<stdio.h> 
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
			scanf("%c",&a[i][j]);
		}
		scanf("\n");
	}
	int m=0;
	if(n%2==0)
	{ 
		m=n/2;
	}
	else
	{
		m=(n/2);
	}
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(n%2!=0 && i==m && j==m)
				printf("* ");
			else if(n%2==0 &&((i==m-1 && j==m-1)||(i==m && j==m)||(i==m && j==m-1)||(i==m-1 && j==m)))
				printf("* ");
			else if(i==0 || j==0 || i==n-1 || j==n-1 || i==m || j==m) 
				printf("*");
			else if(i==0||j==0||i==n-1||j==n-1)
				printf("* ");
			else
				printf("%c",a[i][j]);
		}
		printf("\n");
	}
}
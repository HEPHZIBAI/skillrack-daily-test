/*
The program must accept two integers X and Y (where X != Y) as the input. The program must print all the factors of X which are not the factors of Y as the output.

Boundary Condition(s): 
	2 <= X Y <= 10^6

Input Format:
	The first line contains X and Y separated by a space.

Output Format:
	The first line contains the factors of X which are not the factors of Y.

Example Input/Output 1:
	Input 
		12 14
	Output 
		3 4 6 12
	Explanation:
		The factors of 12 are 12346 12.
		Here 1 and 2 are the factors of 14. So they are not printed.
		Hence the output is 3 4 6 12

Example Input/Output 2:
	Input 
		100 50
	Output 
		4 20 100
*/
#include<stdio.h> 
#include<stdlib.h>

int main()
{
	int x,y;
	scanf("%d%d", &x,&y); 
	int a[10000];
	int k=0; 
	for (int i=2;i<=x;i++)
	{
		if(x%i==0 && y%i!=0)
		{
			a[k]=i; 
			k++;
		}	
	}
	for(int i=0;i<k;i++) 
		printf("%d", a[i]);
}
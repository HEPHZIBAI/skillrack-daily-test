/*
The program must accept N integers as the input. The program must print the integer which is having the maximum number of factors among the N integers as the output. If more than one integer is having the same maximum number of factors then the program must print the largest integer among those integers as the output.

Boundary Condition(s):
	2 <=N<= 10^4
	1 Each integer value <= 10^4

Input Format:
	The first line contains N. The second line contains N integers separated by a space.

Output Format:
	The first line contains the integer based on the given conditions.

Example Input/Output 1:
	Input:
		5
		10 45 8 121 100
	Output:
		100
	Explanation:
		The factors of 10 are 1 2 5 and 10, the factors count is 4. 
		The factors of 45 are 1 359 15 and 45, the factors count is 6.
		The factors of 8 are 1 2 4 and 8, the factors count is 4. 
		The factors of 121 are 1 11 and 121, the factors count is 3.
		The factors of 100 are 1245 10 20 25 50 and 100, the factors count is 9.
		So 100 has the maximum number of factors. Hence the output is 100

Example Input/Output 2:
	Input:
		4
		13 7 29 2
	Output:
		29
*/


#include<stdio.h> 
#include<stdlib.h>

int main()
{
	int n,p; 
	scanf("%d",&n);
	int a[n]; 
	int s=0,l=0,m; 
	for (int i=0;i<n;i++) 
	{
		scanf("%d", &p);
		m=0;
		for (int i=1;i<p;i++)
		{
			if(p%i==0)
				m++;	
		}
		if(m>1)
		{
			l=m;
			s=p;
		}
		else if(m=1)
		{
			if(s<p)
				s=p
		}
	}
	printf("%d",s);
}
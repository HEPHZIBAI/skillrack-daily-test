/*
The program must accept N integers as the input. The program must print the sum of integers containing at least two odd digits among the N integers as the output

Boundary Condition(s):
	1 <= N <= 10^4
	1 < Each integer value <= 10^4

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

OutputFormat:
	The first line contains the sum of integers containing at least two odd digits.

Example Input/Output 1:
	Input
		5
		78 549 123 877 214
	Output:
		1549
	Explanation:
		In the given 5 integers, 549 123 and 877 are having at least 2 odd digits.So the sum of those integers is 1549.Hence the output is 1549

Example Input/Output 2
	Input
		4
		124 4266 184 42
	Output
		0
*/


#include<stdio.h>
#include<stdlib.h>
int main()
{	
	int n;
	scanf("%d", &n);
	int a[n];
	for (int i=0;i<n;i++)
		scanf("%d", &a[i]);
	int t,s=0,c=0,m;
	for (int i=0;i<n;i++)
	{
		C=0;
		t=a[i];
		while(t> 0 && c<2)
		{
			m=t%10;
			t/=10;
			if(m%2!=0)
				c++;
		}
		if(c>=2)
			s+=a[i];

	}
	printf("%d",s);
}
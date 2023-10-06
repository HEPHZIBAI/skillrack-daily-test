/*
The program must accept N integers and a nonzero digit D as the input. The program must print the sum of integers starting with the digit D among the N integers as the output.

Boundary Condition(s) 
	1 <= N <= 100
	1 < Each integer value <= 10^7

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space. The third line contains D.

Output Format:
	The first line contains the sum of integers starting with the digit D among the N Integers.

Example Input/Output 1:
	Input
		5
		15 78 12 17 511
	Output
		44
	Explanation:
		Integers starting with the digit 1 are 15, 12 and 17. So their sum 44 is printed as the output.

Example Input/Output 2:
	Input:
		4	
		54 298 121 657
		7
	Output:
		0
*/


#include<stdio.h> 
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n); 
	int a[n];
	for (int i=0;i<n;i++)
		scanf("%d",&a[i]);
	int d; 
	scanf("%d", &d); 
	for (int i=0;i<n;i++)
	{
		int t; 
		int s=0;
		t=a[i];
		while(t>=10)
			t/-10;
		if(t==d)
			s+a[i];

	}
	printf("%d",s);
}
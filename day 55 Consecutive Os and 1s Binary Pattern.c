/*
The program must accept an integer N as the input. The program must find the binary representation of N and print the desired pattern as shown in the Example Input/Output section

Boundary Condition(s):
	1 <= N <= 10^17

Input Format:
	The first line contains N

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section

Example Input/Output 1:
	Input
		463
	Output:
		111
		00
		1111
	Explanation:
		The binary representation of 463 is 111001111

Example Input/Output 2:
	Input
		81
	Output
		1
		0
		1
		000
		1
	Explanation:
		The binary representation of 81 is 1010001.
*/


#include<stdio.h> 
#include<stdlib.h>

int main()
{
	Long int n;
	scanf("%d",n);
	int a[10000];
	Long int k=0;
	while(n>0)
	{
		a[k]=n%2;
		n/=2;
		k++;
	}
	while(k>=0)
	{
		while(k>=0 && a[k]==1)
		{
			printf("%d",a[k]);
			k--;
		}
		if(k>0) 
			printf("\n");
		while(k>=0 && a[k]==0)
		{
			printf("%d",a[k]);
			k--;
		}
		printf("\n");
	}
}
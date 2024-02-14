/*
The program must accept an integer N as the input. The program must print the sum of each digit to the power of number of digits in N as the output.

Boundary Condition(s):
	1 <= N <= 10^8

Input Format:
	The first line contains N.

Output Format:
	The first line contains the sum of each digit to the power of number of digits in N.

Example Input/Output 1:
	Input:
		154
	Output: 
		190
	Explanation:
		The number of digits in 154 is 3.
		(1 * 1 * 1) + (5 * 5 * 5) + (4 * 4 * 4)
		Hence the output is 190

Example Input/Output 2:
	Input:
		6047
	Output: 
*/



﻿

#include<stdio.h>
#include<stdlib.h> 
#include<math.h> 

int main()
{
	Long int n;
	scanf("%ld", &n);
	int a[10000001]; 
	int s=0,k=0;
	
	while(n>0)
	{
		a[k]=n%10;
		k++;
		n/=10;
	}

	for(int i=0;i<k;i++)
	{
		s+=pow(a[i],k);
	}
	printf("%d",s);
}
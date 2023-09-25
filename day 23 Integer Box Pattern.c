/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	1 <= N <= 10^17

Input Format: 
	The first line contains N.

OutputFormat:
	The first three lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
		45
	Output
		+--+
		|45|
		+--+

Example Input/Output 2:
	Input: 
		12045
	Output
		+-----+
		|12045|
		+-----+
*/

#include<stdio.h> 
#include<stdlib.h>

int main()
{
	Long int a; 
	scanf("%ld", &a); 
	Long int t-a; 
	int s=0;
	while(t>0) 
	{
		t/=10;
		S++;
	}
	printf("+");
	for (int i=0;i<s;i++) 
		printf("-"); 
	printf("+\n|%ld\n",a);
	for (int i0;i<s;i++) 
		printf("-");
	printf("+");
}
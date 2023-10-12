/*
The program must accept an integer N as the input. The program must print the integer N in the ordinal form as the output.

Boundary Condition(s): 
	1 <= N <= 1000

Input Format: 
	The first line contains N.

Output Format:
	The first line contains N in ordinal form.

Example Input/Output 1:
	Input 
		96
	Output
		96th
	Explanation:
		The ordinal form of 96 is 96th. Hence the output is 96th

Example Input/Output 2:
	Input
		1
	Output
		1st
*/

#include<stdio.h> 
#include<stdlib.h>
int main()
{
	int n;
	scanf("%d",&n);
	int k=n%10;
	if(n==1 || k==1 && n!-11) 
		printf("%dst",n);
	else if(n>=4 && n<=20) 
		printf("%dth",n);
	else if(k==2) 
		printf("%dnd",n);
	else if(k==3)
		printf("%drd", ",n); 
	else
		printf("%dth",n);
}
/*
The program must accept an integer N as the input. The program must toggle the last occurring 1 in the binary representation of N. Then the program must print the modified value of N as the output.

Boundary Condition(s): 
	1 <= N < 2^31

Input Format: 
	The first line contains N.

Output Format:
	The first line contains the modified value of N.

Example Input/Output 1:
	Input: 
		10
	Output: 
		8
	Explanation:
		The binary representation of 10 is 1010.
		The last occurring 1 in 1010 is toggled to 0. So the binary representation becomes 1000.
		Now the decimal equivalent of 1000 is 8.
		Hence the output is 8

Example Input/Output 2:
	Input: 
		16
	Output
		0
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n);
	int a[1000000];
	int k=0,m;
	while(n>0) 
	{
		m=n%2;
		a[k]=m;
		k++;
		n/=2;
	}
	
	int i=0,s=0;
	
	while(a[i]!=1 && i<k) 
		i++;

	a[i]=0;
	m=1;

	for(i=0;i<k;i++)
	{
		s=s+(a[i]*m);
		m*=2;
	} 
	printf("%d",s);
}
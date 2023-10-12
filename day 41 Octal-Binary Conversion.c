/*
The program must accept an integer N representing the octal representation of an integer X as the input. The program must print the binary representation of X as the output.

Note: N is always a valid octal representation.

Boundary Condition(s):
	1 <= N <= 10^6
Input Format:
	The first line contains N.
Output Format: 
	The first line contains the binary representation of X.

Example Input/Output 1:
	Input 
		14
	Output 
		1100
	Explanation: 
		14 is the octal representation of 12. So the binary representation of 12 is 1100. Hence the output is 1100

Example Input/Output 2:
	Input
		11
	Output
		1001
*/


#include<stdio.h> 
#include<stdlib.h>
int main()
{	
	int n; 
	scanf("%d", &n); 
	int o=0;
	int p=1,t; 
	while(n>0)
	{
		t=n%10;
		o+=(t*p);
		p*=8; 
		n/=10;
	} 
	int a[10000];
	int k=0;
	while(o>0)
	{
		a[k]=o%2;
		o/=2;
		k++;
	}
	k--;
	while(k>=0)
	{
		printf("%d", a[k]);
		k--;
	}
}
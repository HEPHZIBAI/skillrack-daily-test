/*
The program must accept an integer N as the input. The program must print YES if N is a valid octal representation. Else the program must print NO as the output.

Boundary Condition(s): 
	1 <= N <= 10^7

Input Format: 
	The first line contains N.

Output Format:
	The first line contains YES or NO.

Example Input/Output 1:
	Input
		45
	Output 
		YES
	Explanation:
		The decimal equivalent of (45) is 37 So 45 is a valid octal representation.
		Hence the output is YES

Example Input/Output 2:
	Input 
		814
	Output: 
		NO
*/


#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n);
	int f=0; 
	while(n>0)
	{
		int k=n%10; 
		if(!(k> 0 && k<=7))
		{
			f=1;
			break;
		} 
		n/=10;
	}
	printf(f==0?"YES" : "NO");
}
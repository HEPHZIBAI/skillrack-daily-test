/*
The program must accept an integer N as the input. The program must print YES if all the digits in N are in ascending order. Else the program must print NO as the output

Boundary Condition(s): 
	10 <= N <= 10^7

Input Format: 
	The first line contains N.

Output Format: 
	The first line contains either YES or NO.

Example Input/Output 1:
	Input: 
		2579
	Output 
		YES
	Explanation 
		In 2579 all the digits are in ascending order. So YES is printed as the output

Example Input/Output 2:
	Input:
		52738
	Output
		NO
*/
#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n;
	scanf("%d",&n);
	int a[1000];
	int k=0;
	while(n>0)
	{
		a[k]=n%10;
		n/=10;
		k++;
	}
	int f=1;
	for(int i=0;i<k-1;i++)
	{
		if(a[i]<a[i+1]) 
		{
			f=0;
			break;
		}
	}
	printf(f?"YES": "NO");
}
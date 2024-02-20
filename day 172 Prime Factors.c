/*
The program must accept an integer N as the input. The program must print the prime factors of N in ascending order as the output.

Boundary Condition(s):
	10 <= N <= 10^5

Input Format:
	The first line contains N.

Output Format:
	The first line contains the prime factors of N in ascending
order.

Example Input/Output 1:
	Input:
		100
	Output: 
		2 5
	Explanation:
		The factors of 100 are 1, 2, 4, 5, 10, 20, 25, 50 and 100.
		The prime factors of 100 are 2 and 5.
		So 2 and 5 are printed as the output.

Example Input/Output 2:
	Input:
		150
	Output: 
		2 3 5
*/


#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d", &n);
	for(int i=2;i<=n;i++)
	{
		if(n%i==0)
		{
			int f=1;
			for(int j=2;j<i;j++)
			{
				if(i%j==0)
				{
					f=0;
					break;
				}
			}
			if(f)
				printf("%d ",i);
		}
	}
}

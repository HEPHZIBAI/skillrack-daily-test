
/*
The program must accept an integer N as the input. The program must print the sum of prime integers from 1 to N ending with 7 as the output.

Boundary Condition(s):
	10 <= N <= 10^8

Input Format:
	The first line contains N.

Output Format:
	The first line contains the sum of prime integers from 1 to N ending with 7.

Example Input/Output 1:
	Input: 
		42
	Output: 
		61
	Explanation:
		The prime integers from 1 to 42 which ends with 7 are 7,17 and 37.
		The sum of 7. 17 and 37 is 61
		Hence the output is 61

Example Input/Output 2:
	Input:
		156
	Output: 
		643
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%ld", &n);
	Long int m,s=0;
	for (long int i=7;i<n;i+=10)
	{
		m=1;
		for (long int j=2;j<i;j++)
		{
			if(i%j==0)
			{
				m=0;	
				break;
			}
		}
		if(m)
			s+=i;	
	}
	printf("%ld",s);
}
/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s): 
	3 <= N <= 100

Input Format:
	The first line contains N.

Output Format:
	The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
		9
	Output
		*#######*
		#*#####*#
		##*###*##
		###*#*###
		####*####

Example Input/Output 2:
	Input:
		14
	Output:
		*############*
		#*##########*#
		##*########*##
		###*######*###
		####*####*####
		#####*##*#####
		######**######
	
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n);
	int k=n/2,f=n-2;
	if(n%2!=0)
		k++;
	for(int i=0;i<k;i++)
	{
		for(int j=0;j<i;j++)
		{
			printf("#");
		}
		printf("*");
		
		for(int j=0;j<f;j++)
		{
			printf("#");
		}
		
		if(i!=k-1 || h%2==0)
			printf("*");
		
		f-=2;

		for(int j=0;j<i;j++)
		{
			printf("#");
		}
		printf("\n");
	}
}
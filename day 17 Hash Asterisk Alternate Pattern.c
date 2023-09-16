/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary condition(s): 
	2 <= N <= 100

Input Format:
	The first line contains N.

Output Format:
	The first N lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
		4
	Output
		#*#*
		*#*#
		#*#*
		*#*#

Example Input/Output 2:
	Input
		5	
	Output
		#*#*#
		*#*#*
		#*#*#
		*#*#*
		#*#*#
*/




#include<stdlib.h>
#include<stdio.h>
int main()
{
	int a;
	char k='*'; 
	scanf("%d",&a);
	for (int i=1;ica;i++) 
	{
		if (i%2==0)
			k='*';
		else
			k='#'
		for (int j=1;j<=a;j++)
		{
			printf("%c",k);
			if(k=='#')
				k='*';
			else
				k='#';
		}
		printf("\n");
	}
}
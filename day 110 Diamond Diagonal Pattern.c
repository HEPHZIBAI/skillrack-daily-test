/*
The program must accept an integer N and a character CH as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s): 
	4 <= N <= 50

Input Format:
	The first line contains N and CH separated by a space.

Output Format:
	The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input 
		5 *
	Output:
		----*
		---***
		--*-*-*
		-*--*--*--*
		***********

Example Input/Output 2:
	Input
		6 #
	Output:
		-----#
		----###
		---#-#-#
		--#--#--#
		-#---#---#
		##########		
		-#---#---#
		--#--#--#
		---#-#-#
		----###
		-----#
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n,f;
	char a,c;
	scanf("%d %c",&n,&a);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n-i-1;j++)
			printf("-");
	} 
	if(i==0)
		printf("%c",a);
	else
	{
		f=0;
		while(f<3)
		{
			printf("%c",a);
			if(f!=2)
			{
				if(i==n-1)
					c=a;
				else
					c='-';
				for(int k=0;k<i-1;k++)
					printf("%c",c);
			}
			f++;
		}
		printf("\n");
	}
	for(int i=0;i<n-1;i++)
	{
		for(int j=0;j<i;j++)
		{
			printf("-");
		}
		f=0;
		if(i!=n-2)
		{
			while(f<3)
			{
				printf("%c",a);
				if(f!=2)
				{
					for(int j=0;j<n-i-3;j++)
						printf("-");
				}
				f++;
			}
		}
		else
			printf("%c",a); 
		printf("\n");
	}
}
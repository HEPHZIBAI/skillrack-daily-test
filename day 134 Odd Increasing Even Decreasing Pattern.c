/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s): 
	1 <= N <= 500

Input Format:
	The first line contains N.

Output Format:
	The first N lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
		5
	Output
		----1
		---131
		--13531
		-1354531
		135424531

Example Input/Output 2:
	Input
		8
	Output
		-------1
		------131
		-----13531
		----1357531
		---135787531
		--13578687531
		-1357864687531
		135786424687531
*/

#include<stdio.h>
#include<stdlib.h>

int main() 
{
	int n;
	scanf("%d",&n);
	int k=1,m;

	if(n%2==0)
	{
		for(int i=1;i<=n;i++)
		{
			k=1;
			m=n;

			for(int j=0;j<n-i;j++)
				printf("-");

			for(int j=0;j<i;j++)
			{
				if(k<=n)
				{
					printf("%d",k);
					k+=2;
				}
			}
			
			if(i>n/2)
			{
				for(int j=0;j<i-(n/2);j++)
				{
					printf("%d",m);
					m-=2;	
				}

				m+=2;
				for(int j=0;j<i-(n/2)-1;j++)
				{
					m+=2;
					printf("%d",m);
				}
			}
			k-=2;
			if(i<=n/2)
			{
				for(int j=0;j<i-1;j++)
				{
					k-=2;
					printf("%d",k);
				}
			}
			else
			{
				for(int j=0;j<n-(n/2);j++)
				{
					printf("%d",k);
					k-=2;
				}
			}
			printf("\n");
		}
	}
	else
	{
		for(int i=1;i<=n;i++)
		{
			k=1;
			m=n-1;
			for(int j=0;j<n-1;j++)
			{	
				printf("-");
			}
			for(int j=0;j<i;j++) 
			{
				printf("%d",k);
				k+=2;
				if(k>n)
					break;
			} 
			if(i>=(n/2)+2)
			{
				for(int j=0;j<1-(n/2)-1;j++)
				{
					printf("%d",m);
					m-=2;
				}
				m+=2;
				for(int j=0;j<i-(n/2)-2;j++)
				{
					m+=2;
					printf("%d",m);
				}
				k=n;		
				for(;k>=1;k-=2) 
					printf("%d",k);
			}
			else
			{
				k-=2;
				for (int j=0;j<i-1;j++)
				{ 
					k-=2;
					printf("%d",k);	
				}
			}
			printf("\n");
		}
	}
}
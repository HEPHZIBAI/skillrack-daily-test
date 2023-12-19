/*
The program must accept two odd integers X and Y as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s): 
	3 <=X,Y <= 99

Input Format:
	The first line contains X and Y separated by a space.

Output Format:
	The first X lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
		5 5
	Output
		* * * * *
		* 0 * 0 *
		* * * * *
		* 0 * 0 *
		* * * * *

Example Input/Output 2:
	Input 
		3 5
	Output
		* * * * *
		* 0 * 0 *
		* * * * *
	
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int x,y; 
	scanf("%d%d",&x,&y);
	for(int i=1;i<=x;i++)
	{
		if(i%2!=0)
		{
			for(int j=0;j<y;j++) 
				printf("* ");
		}
		else
		{
			for(int j=1;j<=y;j++)
			{
				if(j%2!=0) 
					printf("* "); 
				else 
					printf("0 ");
			}
		}
		printf("\n");
}
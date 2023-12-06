/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	1 <= N <= 17

Input Format:
	The first line contains N.

Output Format:
	The first N lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
		5
	Output
		5555555555555555
		4444444411111111	
		3333222233332222
		2233223322332233
		1414141414141414

Example Input/Output 2:
	Input:
		4
	Output
		44444444
		33331111
		22222222
		13131313

Example Input/Output 3:
	Input
		6
	Output
		66666666666666666666666666666666
		55555555555555551111111111111111
		44444444222222224444444422222222
		33332222333322223333222233332222
		22442244224422442244224422442244
		15151515151515151515151515151515
*/


#include<stdio.h> 
#include<stdlib.h>
#include<math.h>

int main()
{
	int n;
	scanf("%d",&n); 
	int k=pow(2, (n-1));
	int h=n-1,m=1,z=1,l=1; 
	for(int i=1;i<=n;i++)
	{
		k=pow(2,h);
		for(int f=1;f<=m;f++)
		{
			if(f%2!=0)
			{
				for(int j=0;j<k;j++)
					printf("%d",h+1);
			}
			else
			{
				for(int j=0;j<k;j++) 
					printf("%d",l-1);
			}
		}
		printf("\n");
		h--;
		h--;
		m=pow(2,z);
		z++;
		l++;
	}
}
/*
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	10 <= N <= 10^16

Input Format: 
	The first line contains N.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
		9165
	Output
		9165
		165
		65
		5

Example Input/Output 2:
	Input:
		108004
	Output:
		108004
		8004
		8004
		4
		4
		4
*/


#include<stdio.h>
#include<stdlib.h>
int main()
{
	Long int n; 
	scanf("%ld", &n); 
	printf("%ld\n",n); 
	int a[100]; 
	int k=0; 
	while(n>0)
	{
		a[k]=n%10; 
		n/=10;
		k++;
	}
	int j,m;
	for (int i=k-2;i>=0;i--)
	{
		j=i;
		m=1;
		while(a[j]==0 && j>=0)
		{
			j--;
		}	
		for (;j>=0;j--) 
		{
			printf("%d",a[j]);
			m=0;
		}
		if(m)
			printf("0"); 
		printf("\n");
	}
}
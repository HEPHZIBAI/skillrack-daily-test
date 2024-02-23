/*
The program must accept the price P of an item as the input. The program must print the minimum number of coins needed to purchase the item as the output. The denominations of the coins are given below. 1000, 500, 100, 50, 20, 10, 5 and 1.

Boundary Condition(s):
	1 <= P <= 10^12

Input Format:
	The first line contains P.

Output Format:
	The first line contains the minimum number of coins needed to purchase the item.

Example Input/Output 1:
	Input:
		1593
	Output: 
		8
	Explanation:
		1593 = (1000 * 1) + (500 * 1) + (50 * 1) + (20 * 2) + (1 * 3)

Example Input/Output 2:
	Input:
		24892
	Output: 
		33
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int c=0;
	Long int n;
	scanf("%ld",&n); 
	while(n>0)
	{
		if(n>=1000)
		{
			c+=1;
			n-=1000;
		}
		else if(n>=500)
		{
			c+=1;
			n-=500;
		}
		else if(n>=100)
		{
			c+=1; 
			n-=100;
		}
		else if(n>=50)
		{
			c+=1;
			n-=50;
		}
		else if(n>=20)
		{
			c+=1;
			n-=20;
		}
		else if(n>=10)
		{
			c+=1;
			n-=10;
		}
		else if(n>=5)
		{
			c+=1;
			n-=5;
		}
		else
		{
			c+=1;
			n-=1;
		}
	}
	printf("%d",c);
}
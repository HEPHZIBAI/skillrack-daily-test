/*
In a staircase, there are infinite number of steps. A boy is standing in the Xth step and he wants to go to the yth step. The boy can move 1 step or 2 steps or 5 steps in a jump (either in upward or downward). The program must accept the values of X and Y as the input. The program must print the minimum number of jumps required by the boy to reach yth step from the Xth step in the staircase as the output

Boundary Condition(s): 
	0 <= X, Y <= 10^9

Input Format:
	The first line contains X and Y separated by a space.

Output Format:
	The first line contains the minimum number of jumps required by the boy.

Example Input/Output 1:
	Input
		5 12
	Output 
		2

Explanation:
	One possible way of reaching the 12th step from the 5th step is given below. 
	5 steps up -> 2 steps up 
	Here 2 jumps are required by the boy, so 2 printed as the output.

Example Input/Output 2:
	Input
		8 0
	Output:
		3

Example Input/Output 3:
	Input:
		20 43
	Output: 
		6
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	long long int x,y,c=0;
	scanf("%lld %lld",&x,&y);
	c=abs(x-y);
	int a=0;
	while(c>4)
	{
		a++;
		c-=5;
	}
	while(c>1)
	{
		a++;
		c-=2;
	}
	while(c>0)
	{
		a++;
		c--;
	}
	printf("%d",a);
}
/*
The program must accept two integers X and Y as the input. The program must swap the first digit of X and the last occurring nonzero digit of Y. Then the program must print the sum of X and Y as the output.

Boundary Condition(s):
	1 <= X Y <= 10^8

Input Format:
	The first line contains X and Y separated by a space.

Output Format:
	The first line contains the sum of X and Y as per the given condition.

Example Input/Output 1:
	Input 
		524 1200
	Output: 
		1724
	Explanation:
		The first digit of 524 is 5.
		The last occurring nonzero digit of 1200 is 2.
		After swaping those two digits, the integers become 224 and 1500. So their sum 1724 is printed as the output.

Example Input/Output 2:
	Input:
		1000 2000
	Output
		3000

*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int x,y;
	scanf("%d%d",&x,&y ) ;
	int a = x, b = y;
	int u = 0, s = 1
	if(y>0 && y% * 10 ==0)
	{
		y /=10;
		s*=10;
	}
	u = y%10
	y /=10:
	int d=1;
	while(x>=10)
	{
		d*= 10
		x/=10;
	}
	y=((y*10)+x)*s;
	u=(u*d)+(a%d);
	printf("%d",y+u);
}
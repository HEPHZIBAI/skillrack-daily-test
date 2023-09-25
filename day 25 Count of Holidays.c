/*
The program must accept an integer N representing the number of days as the input. The program must print the minimum and maximum possible number of holidays present in the given N days if saturday and sunday are holidays. Hint: The first day in the given N days can be any one among the 7 week days.

Boundary Condition(s):
	1 <= N <= 100

Input Format:
	The first line contains N.

Output Format: 
	The first line contains the minimum and maximum possible number of holidays separated by a space.

Example Input/Output 1:
	Input
		10
	Output
		24
	Explanation:
		The minimum possible number of holidays 2 is obtained if the 1st day starts from Monday.
		The maximum possible number of holidays 4 is obtained if the 1st day starts from Saturday
		Hence the output is 24

Example Input/Output 2:
	Input
		7
	Output
		22
*/
#include<stdio.h> 
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n);
	int x=6; 
	int y=1;
	int m=n;
	int min=0;
	int max=0; 
	while(n>0)
	{
		if (y==6||y==7)
			min++;
		y++; 
		if(y==8)	
			y=1;
		if(x==6 ||x==7)
			max++;
		x++;
		if(x==8)
			x=1;
		n--;
	}	
	printf("%d %d", min, max);
}
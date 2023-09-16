/*
The program must accept two integers X and Y as the input. The program must print the integers from X to Y which are formed only using the odd digits. If there is no such integer then the program must print -1 as the output

Boundary Condition(s): 
	1 <= X Y <= 10^7

Input Format:
	The first line contains X and Y separated by a space.
Output Format:
	The first line contains the integers from X to Y which are formed using the odd digits or-1.

Example Input/Output 1:
	Input 
		10 30
	Output 
		11 13 15 17 19
	Explanation:
		The integers from 10 to 30 are 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
		The integers which are formed using the odd digits are 11 13 15 17 19.
		Hence the output is 11 13 15 17 19
	
Example Input/Output 2
	Input 
		3253 3297
	Output
		-1
*/



#include<stdio.h> 
#include<stdlib.h>
int main()
{
	int x,y; 
	scanf("%d%d",x,y); 
	int f=0; 
	int l;
	int m=1;
	for(;x<=y;x++)
	{
		f=1;
		l=x;
		while(l>0)
		{
			if((l%10)%2==0)
			{
				f=0;
				break;
			}
			l/=10;
		}
		if(f) 
		{
			printf("%d",x);
			m=0;
		}
	}
	if(m) 
		printf("-1");
}
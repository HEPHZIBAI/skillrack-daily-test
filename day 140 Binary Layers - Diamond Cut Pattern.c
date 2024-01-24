/*
The program must accept an integer N as the input. The program must
print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	1 <= N <= 100

Input Format:
	The first line contains N.
Output Format:
	The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		5
	Output:
		####1
		###000
		##11111
		#0100010
		101010101
		#0100010
		##11111
		###000
		####1
	Explanation:
		The binary layers pattern for 5 is given below.
		111111111
		100000001
		101111101
		101000101
		101010101
		101000101
		101111101
		100000001
		111111111
		Here, the diamond part of the above pattern is printed as the output.


Example Input/Output 2:
	Input:
		4
	Output:
		###0
		##111
		#10001
		0101010
		#10001
		##111 
		###0

*/

#include<stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	int t=n;
	int ml=(n*2)-1;
	int b[ml][ml],v,k=n-1,f=n-1;
	for(int i=0;i<ml;i++)
	{
		if(n%2!=0)
			v=(i%2==0)?1:0;
		else
			v=(i%2==0)?0:1;
		for(int j=i;j<ml-i;j++)
		{
			b[i][j]=v;
			b[j][i]=v;
			b[ml-i-1][j]=v;
			b[j][ml-i-1]=v;
		}
	}

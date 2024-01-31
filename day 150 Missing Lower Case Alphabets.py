'''
The program must accept two string values S1 and S2 containing only lower case alphabets as the input. The program must print the missing lower case alphabets among the alphabets in S1 and S2 in alphabetical order. If all the lower case alphabets are present in S1 and S2, the program must print -1 as the output.

Boundary Condition(s):
	1 <= Length of S1, S2 <= 100

Input Format:
	The first line contains S1.The second line contains S2.

Output Format:
	The first line contains the missing alphabets or -1.

Example Input/Output 1:
	Input:
		hello
		skillrack
	Output
		bdfgjmnpqtuvwxyz
	Explanation:
		The missing lower case alphabets in "hello" and "skillrack" are b, d, f, g, j,m, n, p, q, t, u, v, w, x, y and z.
		Hence the output is bdfgjmnpqtuvwxyz

Example Input/Output 2:
	Input:
		abcdefghijklmn
		opqrstuvwxyz
	Output: 
		-1
'''


#include<stdio.h>
﻿#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n);
	int a[n][n];
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
			scanf("%d",&a[i][j]);
	}
	int s=0,l=0;
	for(int i=0;i<n/2;i++)
	{
		s=0;
		int j=i;
		for(;j<n-i;j++)
			s+=a[i][j];
		j=i;
		for(;j<n-i;j++)
			s+=a[j][n+i-1];
		j=i;
		for(;j<n-i;j++)
			s+=a[n-i-1][j];
		j=i;
		for(;j<n-i;j++)﻿
			s+=a[j][i];
		if(s>l)
			l=s;
	}
	printf("%d",l);
}
/*
The program must accept N integers separated by an alphabet as the program must print the sum of those N integers as the output.

Boundary Condition(s):
	2 <= N <= 100
	1 <= Each integer value <= 10^7

Input Format:
	The first line contains N.
	The second line contains N integers separated by an alphabet.

Output Format:
	The first line contains the sum of N integers.

Example Input/Output 1:
	Input:
		4
		10a5w240n23
	Output:
		278
	Explanation:
		The four integers are 10, 5, 240 and 23. So their sum is 278.

Example Input/Output 2:
	Input
		5
		1s2d3h4e4
	Output:
		14
*/


#include<stdio.h> 
#include<stdlib.h>
int main()
{
	int n;
	char a[10000000]; 
	scanf("%d\n%s", &n,a); 
	int s=0; 
	int f; 
	for(int i=0;i<strlen(a);i++)
	{
		f=0; 
		while(i<strlen(a) && ((a[i]>='a'&&a[i]<='z') ||a[i] >='A'&&a[i] <= 'Z'))
		{
			i++;
		}
		while(i<strlen(a) && ! ( (a[i]>='a'&&a[i]<='z')||(a[i] >='A'&&a[i] <='Z')))		{
			int l=a[i]-'0';
			f=(f*10)+l; 
			i++;
		}
		s+=f;
		printf("%d ",f);
	} 
	printf("%d",s);
}
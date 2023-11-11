/*
The program must accept N integers as the input. The program must swap every two odd integers in their positions among the N integers. The program must print the revised values of N integers as the output. If the number of odd integers in the given N integers is odd then the program must keep that last odd integer as it is.

Boundary Condition(s):
	2 <= N = 1000
	1 < Each integer value <= 10^5

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format:
	The first line contains the revised values of N integers separated by a space.

Example Input/Output 1:
	Input
		7
		22 23 51 56 69 53 29
	Output
		22 51 23 56 53 69 29
	Explanation:
		After swapping the first two odd integers 23 and 51 in the given 7 integers, the integers become 22 51 23 56 69 53 29. After swapping the last two odd integers 69 and 53 in the given 7 integers, the integers become 22 51 23 56 53 69 29. Hence the output is 22 51 23 56 53 69 29

Example Input/Output 2:
	Input:
		5
		3 4 7 21 89
	Output:
		7 4 3 89 21
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n;
	scanf("%d",&n);
	int a[n]; 
	int b[n],c[n], k=0; 
	for (int i=0;in;i++)
	{
		scanf("%d",&a[i]);
		if(a[i]%2!=0)
		{
			b[k]=a[i];
			c[k]=i;
			k++;
		}
	}
	int t;
	for(int i=0;i<k-1;i+=2)
	{
		t=a[c[i+1]]; 
		a[c[i+1]]=a[c[i]]; 
		a[c[i]]=t;
	}
	for(int i=0;i<n;i++)
	{
		printf("%d ",a[i]);
	}
}
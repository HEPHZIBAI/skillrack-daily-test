/*
The program must accept an integer array of size N and an integer K as the input. The program must print the output based on the following conditions.
	- After sorting the first K integers in the array, if all the
integers in the array in sorted order then the program must print YES.
	- Else the program must print NO as the output.

Boundary Condition(s):
	2 <= N <= 100
	1 <= Each integer value <= 10^5
	2 <= K <= N

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space. The third line contains K.

Output Format:
	The first line contains YES or NO.

Example Input/Output 1:
	Input:
		9
		39 23 19 27 41 55 69 88 97
		4
	Output: 
		YES
	Explanation:
		The 9 integers are 39 23 19 27 41 55 69 88 97.
		After sorting the first 4 integers in ascending order, the integers become 19 23 27 39 41 55 69 88 97.
		Now, all the 9 integers are in ascending order. So YES is printed.

Example Input/Output 2:
	Input:
		5
		25 39 41 85 27
		3
	Output: 
		NO
*/



#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n,k;
	scanf("%d%d",&n,&k); 
	int a[n];
	
	for(int i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n-1;j++)
		{
			if(a[j]<a[j+1])
			{
				int t=a[j];
				a[j]=a[j+1];
				a[j+1]=t;
			}
		}
	}
}



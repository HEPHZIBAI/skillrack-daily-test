/*
The program must accept two lines of N integers each as the input. The program must print the odd integers from both the lines based on their order of occurrences as the output. If both lines having odd integers in the same position then print the odd integer from the first line followed by the odd integer from the second line.

Boundary Condition(s):
	1 <= N <= 100
	1 <= Each integer value <= 1000

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.
	The third line contains N integers separated by a space.

Output Format:
	The first line contains the odd integers based on their order of occurrences.

Example Input/Output 1:
	Input
		5
		11 10 12 13 77
		45 44 44 43 10
	Output
		11 45 13 43 77
	Explanation:
		The odd integers in the 1st line are 11 13 and 77. The odd integers in the 2nd list are 45 and 43. So, those odd integers are printed based on their order of occurrences. Hence the output is 11 45 13 43 77

Example Input/Output 2:
	Input:
		6
		12 11 14 13 10 20
		8 15 24 22 13 19
	Output
		11 15 13 13 19

Example Input/Output 3:
	Input
		4
		3 1 4 8
		6 2 7 9
	Output
		3 1 7 9
*/

#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n; 
	scanf("%d",&n); 
	int a[n],b[n]; 
	for(int i=0;i<n;i++) 
		scanf("%d",&a[i]); 
	for(int j=0;j<n;j++) 
		scanf("%d",&b[j]);
	for(int i=0;i<n;i++) 
	{
		if(a[i]%2!=0&& b[i]%2!=0) 
			printf("%d %d",a[1],b[i]); 
		else
		{
			if(a[i]%2!=0) 
				printf("%d ",a[i]); 
			if(b[i]%2!=0) 
				printf("%d ",b[i]);
		}
	}
}
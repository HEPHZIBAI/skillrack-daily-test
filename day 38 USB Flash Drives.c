/*
Mr. ABC has X megabytes of documents. He also has N USB flash drives with different capacities to store his documents. The capacity (in megabytes) of each USB flash drive is passed as the input to the program. The value of X is also passed as the input to the program. The program must print the minimum number of USB flash drives that he needs to store his X megabytes of documents. If all the N USB flash drives are not enough to store X megabytes, the program must print -1 as the output.

Note: The size of each document is always 1 megabyte.

Boundary Condition(s):
	1 <= N <= 1000 1 <= Capacity of each USB flash drive, X <= 10^5
inut Format:
	he first line contains N.The second line contains N integers separated by a space.The third line contains X.

Output Format:
	he first line contains the minimum number of USB flash drives that he needs to store his X megabytes of documents.

Example Input/Output 1:
	Input
		5
		3 4 8 1 6
		18
	Output
      		3
	Explanation:
		He needs at least 3 USB flash drives to store 18 megabytes of documents. So 3 is printed as the output.The one possible way of choosing the 3 USB flash drives is 48 and 6.

Example Input/Output 2:
	Input
		2
		5 10
   		11
	Output
		2
Example Input/Output 3:
	Input
		512 1024 64 8
		2048
	Output
		-1
*/

#include<stdio.h> 
#include<stdlib.h>

int main()
{	
	int n; 
	scanf("%d", &n); 
	int a[n]; 
	for (int i=0;i<n;i++) 
	{
		scanf("%d",&a[i]);
	}
	int f; 
	scanf("%d",&f);
	int t;
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<n-1;j++) 
		{
			if(a[j]<a[j+1])
			{
				t=a[j]; 
				a[j]=a[j+1] 
				a[j+1]=t;
			}
		}
	}
	t=0;
	int k=0;
	int s=0;
	while(t<f && k<n)
	{
		t+=a[k];
		k++;
		s++;
	}
	if(t<f)
		printf("-1"); 
	else 
		printf("%d",s);
}
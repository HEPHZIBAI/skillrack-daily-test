/*


In a parking lot, N cars can be parked in a row. The free slots are denoted by a 0 and the occupied slots are denoted by a 1. The program must accept N integers (representing the slots) as the input. The program must print the number of ways two cars can be parked successively.

Boundary Condition(s):
	2 <= N <= 1000

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format:
	The first line contains the number of ways two cars can be parked successively.

Example Input/Output 1:
	Input 
		10
		1 0 0 0 1 0 1 0 0 1
	Output
		3
	Explanation:
		There are 3 ways to park two cars successively 1000101001. In the 300 slots, two cars can be parked in 2 ways.In the slots, two cars can be parked in 1 way. So 3 (2+1) ways are there to park two cars successively. Hence the output is 3

Example Input/Output 2: 
	Input:
		9
		1 0 0 0 0 0 1 0 0
	Output:
	5
*/

#include<stdio.h> 
#include<stdlib.h>
int main()
{
	int n;
	scanf("%d", &n); 
	int s=0; 
	int a[n]; 
	for (int i=0;i<n;i++) 
		scanf("%d",&a[i]);
	for (int i=0;i<n-1;i++)
	{
		if(a[i]==0 && a[i+1]==0)
			s++;
	}
	printf("%d",s);
}
			
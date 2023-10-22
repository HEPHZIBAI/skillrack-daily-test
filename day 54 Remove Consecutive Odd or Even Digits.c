/*
The program must accept an integer N as the input. The program must remove the last occurring consecutive odd digits of N if the last digit of N is odd. Else the program must remove the last occurring consecutive even digits of N. Finally, the program must print the modified integer N as the output.

Note: At least one odd digit and one even digit are always present in the integer N.

Boundary Condition(s): 
	100 <= N <= 10^8

Input Format: 
	The first line contains N.

Output Format:
	The first line contains the modified N.

Example Input/Output 1:
	Input
		2315642
	Output
		2315
	Explanation:
		Here N-2315642. The last digit of 2315642 is even. After removing the last occurring consecutive even digits of 2315642 now the integer become 2315 hence the output is 2315

Example Input/Output 2: 
	Input:
		92423
	Output 
		9242
*/

#includerstdio.h>
#includerstdlib.h>
int main()
{
	Long int a;
	scanf("%d",&a);
	if(a%2==0)
	{
		while(a%2==0)
			a/=10;
	}
	else
	{
		while(a%2!=0)
			a/=10;
	}
	printf("%ld", a);
}
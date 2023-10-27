/*
The program must accept a string S as the input. For each substring containing only vowels in the string S, the program must enclose the substring by a pair of curly braces (). Then the program must print the modified string S as the out.

Boundary Condition(s):
	1 <= Length of S <= 100

Input Format: 
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input 
		bookreading
	Output
		b{oo}kr{ea}d{i}ng

Explanation:
	Here the string is bookreading. The substring containing only vowels in S are oo ea and i. So they are enclosed by the pair of curly braces 0.Hence the output is bloo)kr(ea)d(i)ng

Example Input/Output 2:
	Input:
		AelOu
	Output: 
		{AelOu}

Example Input/Output 3:
	Input:
		Apple
	Output
		{A}ppl{e}
*/

#include<stdio.h>
#include<stdlib.h>
int isv(char x)
{
	if(x=='a'||x=='e'|x=='i'|| x=='o'||x=='u'||x=='A'||x=='E'||x=='I'||x=='O'||x== 'U')
	return 1;
else
	return 0;
int main()
{
	char a[100];
	scanf("%s",a);
	if(isv(a[e]))
		printf("{");
	int m;
	for (int i=0;i<strlen(a);i++)
	{
		m=0;
		if(i!=0 && isv(a[i])) 
			printf("{"); 
		while(isv(a[i]) && i<strlen(a)) 
		{
			printf("%c",a[i]);
			i++;
			m=1;
		}
		if(m)
			printf("}"); 
		if(i<strlen(a)) 
			printf("%c",a[i]);
	}
}
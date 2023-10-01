/*
The program must accept a string $ containing only alphabets as the input. The program must toggle the case of alternate alphabets in the string S. Then the program must print the modified string S as the output.

Boundary Condition(s):
	2 <= Length of S <= 10^5

Input Format:
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input
		SkillRack
	Output: 
		skilLRACK
	Explanation:
		The alternate alphabets in the string kIR ck are 'S', T, T., K. So the case of the alternate alphabets are toggled. Hence the output is skilLRACK
	
Example Input/Output 2:
	Input
		yellow
	Output 
		YeUOw
*/


#include<stdio.h> 
#include<stdlib.h>
int main()
{
	char a[100000]; 
	scanf("%s",a); 
	for (int i=0;i<strlen(a);i++)
	{
		if(i= 0 || i%2==0)
		{
			if(islower (a[i])) 
				printf("%c", toupper(a[i])); 
			else
				printf("%c", tolower(a[i]));
		} 
		else
			printf("%c",a[i]);
	}
}
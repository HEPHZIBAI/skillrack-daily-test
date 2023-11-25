/*
The program must accept a string S containing only alphabets as the input. The program must reverse the string S, keeping the vowels in the same position. Then the program must print the modified string S as the output.

Boundary Condition(s): 
	1 <= Length of S <= 1000

Input Format: 
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input:
		bulk
	Output 
		kulb
	Explanation:
		There is only one vowel in bulk. So the string is reversed exceptu. Hence the output is kulb

Example Input/Output 2:
	Input
		Apple
	Output
		Alppe
*/

include<stdio.h>
#include<stdlib.h>

int main()
{
	char a[1000];
	scanf("%s",a);
	char b[strlen(a)];
	int k=0;
	for(int i=0;i<strlen(a);i++)
	{
		if(!(a[i]=='a'||a[i]=='e'|| a[i]=='i' ||a[i]=='o' ||a[i]=='u'||a[i]=='A'||a[i]=='E'||a[i]=='I'||a[i]=='O'||a[i]=='U')
		{
			b[k]=a[i];
			k++;	
		}
	}
	int l=strlen(a)-1;
	k--;
	for(int i=0;i<strlen(a);i++)
	{
		if(!(a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u'||a[i]=='A'||a[i]=='E'||a[i]=='I'||a[i]=='O'||a[i]=='U')
		{
			printf("%c",b[k]);
			k--;
		}
		else
			printf("%c",e[i]);
	}
}
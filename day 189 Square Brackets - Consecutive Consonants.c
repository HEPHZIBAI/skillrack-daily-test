/*

The program must accept a string S containing only alphabets as the input. The program must enclose the consecutive consonants in the string S within the square brackets (possibly 1 consonant). Then the program must print the modified string S as the output. If there is no consonant in the string S, the program must print the same string as it is.

Boundary Condition(s):
	1 <= Length of S <= 1000

Input Format:
	The first line contains S.

Example Input/Output 1:
	Input:
		skillrack
	Output:
		[sk]i[llr]a[ck]
	Explanation:
		The consecutive consonants in the string skillrack are sk,Ilr and ck.
		So they are enclosed within the square brackets.
		Hence the output is [sk]i[llr]a[ck]

Example Input/Output 2:
	Input:
		CardGames
	Output:
		[C]a[rdG]a[m]e[s]

Example Input/Output 3:
	Input:
		Aeiou
	Output:
		Aeiou
*/

﻿
#include<stdio.h>
#include<stdlib.h>

int vo(char h)
{
	if(h=='a'||h=='e'||h=='i'||h=='o' |│h=='u' ||│h=='A' ||h== 'E' ||h=='I'||h== '0'||h=='U')
		return 1;
	return 0;
}

int main()
{
	char a[1000];
	scanf("%s",a);
	int i=0;

	while(i<strlen(a))
	{
		int m=0;
		while(i<strlen(a) && vo(a[i]))
		{
			printf("%c",a[i]);
			i+=1;
		}
		if(strlen(a)>i)
			printf("[");
		while(i<strlen(a) && !vo(a[i]))
		{
			printf("%c",a[i]);
			i+=1; 
			m=1;
		}
		if(m==1)
			printf("]");
	}
	return 0;
}

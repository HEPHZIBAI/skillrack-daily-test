/*
The program must accept two string values $1 and $2 of equal length as the input. The program must print YES if both the string values have a vowel or a consonant at the same position. Else the program must print NO as the output.

Boundary Condition(s) 
	1 < Length of S1, S2 <= 1000

Input Format:
	The first line contains $1. The second line contains S2.

Output Format:
	The first line contains YES or NO.

Example Input/Output 1:
	Input:
		mcabcdeng 
		SKILLRACK
	Output 
		YES
	Explanation:
		Here both the string values have a vowel or a consonant at the same position. 
		m S-consonants
		c K-consonants
		a I-vowels
		b L-consonants
		c L-consonants
		d R-consonants
		e A-vowels
		n C-consonants
		g K-consonants
		Hence the output is YES

Example Input/Output 2:
	Input:
		yogaa 
		power
	Output:
		NO
*/



#include<stdio.h>
#include<stdlib.h>
int isvo(char l)
{
	l=tolower(l);
	if(l='a' ||l='e' ||l='i' ||l='o' ||l='u' )
		return(1);
	else
		return(0);
}

int main()
{
	char a[1000],b[1000];
	scanf("%s\n%s",a,b);
	int m=1;
	for (int i=0;i<strlen(a);i++)
	{
		if(!(((isvo(a[i]))&&(isvo(b[i]))||((isvo(a[i]))&&(isvo (b[i])))))
		{
			m=0;
			break;
		}
	}
	printf(m==1?"YES":"NO");
}
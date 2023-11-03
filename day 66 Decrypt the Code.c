/*
The program must accept a string S (encrypted string) containing only. (Dots) and. (Hyphens) as the input. The encryption algorithm is given below.
-Digit 0 is encrypted as. (Single Dot).
-Digit 1 is encrypted as (Hyphen and Dot).
-Digit 2 is encrypted as -- (Two Hyphens).
The program must decrypt the string S and print it as the output.
Note: The string S is always a valid encrypted string.

Boundary Condition(s):
	1 <= Length of S <= 1000

Input Format: 
	The first line contains S.

Output Format: 
	The first line contains the decrypted string of S.

Example Input/Output 1:
	Input:
		.-.--
	Output 
		012
	Explanation:
		012 can be decrypted as "-", so 012 is printed as the output.

Example Input/Output 2: 
	Input
		--.
	Output 
		20
*/


#include<stdio.h> 
#include<stdlib.h>

int main()
{
	char a[1000];
	scanf("%s", a);
	for(int i=0;i<strlen(a);i++)
	{
		if(a[i]=='.') 
			printf("0"); 
		else if(a[i]=='-') 
		{
			if(a[i+1]=='.') 
				printf("1"); 
			else
				printf("2");
		}
	}
}
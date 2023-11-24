/*
The program must accept a string $ as the input. The program must print the desired pattern as shown in the Example Input/Output section. Note: The length of S is always odd.

Boundary Condition(s): 
	5 <= Length of S <= 99

Input Format: 
	The first line contains S.

Output Format:
	The lines containing the desired pattern as shown in the Example Inpût/Output section

Example Input/Output 1:
	Input
		12345
	Output
		**1**	
		*2*2*
		34543

Example Input/Output 2: 
	Input
		abcdefg
	Output
		***a***
		**b*b**
		*c***c*
		defgfed

Example Input/Output 3:
	Input:
		skillrack
	Output:
		****s****
		***k*k***
		**i***i**
		*l*****l*
		lrackcarl
*/

#include<stdio.h> 
#include<stdlib.h>

int main()
{
	char a[100];
	scanf("%s",a);
	int l=strlen(a);
	int m=(l/2);
	int h=0,w=0;
	for(int i=0;i<m;i++)
	{
		for(int j=0;j<m-i;j++)
			printf("*");
		printf("%c",a[h]); 
		for(int j=0;j<w;j++)
			printf("*");
		if(i!=e) 
			printf("%c", a[h]); 
		for(int j=0;j<m-i;j++)
			printf("*");
		printf("\n");
		h+=1;
		if(w==0)
			w=1;
		else if(w>-1)
			W+=2;
	}
	w=m;
	for(;m<strlen(a);m++)
		printf("%c",a[m]);
	m=w;
	w+=m;
	w--;	
	for(;w>=m;w--)
		printf("%c",a[w]);
}
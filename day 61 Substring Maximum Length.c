/*
The program must accept two string values S1 and S2 are of equal length as the input. The program must print the common substring which is having the maximum length and occurring at the same position in both string values. If there is more than one such substring then print the first occurring one as the output.
Note: At least one character is always present at the same position in both string values.

Boundary Condition(s):
	1 <= Length of S1, S2 <= 1000

Input Format:
	The first line contains $1.
	The second line contains $2.

Output Format:
	The first line contains the common substring which is having the maximum length and occurring at the same position in both string values.

Example Input/Output 1:
	Input
		skillrack
		SkillRack
	Output:
		kill
	Explanation:
		There are two substrings kill and ack occurring at the same position in both string values.skilrack Skill RackHere the substring kill is having the maximum length. So kill is printed as the output

Example Input/Output 2:
	Input
		abcxxyzmn
		abdryzkmn
	Output:
		ab
*/


#include<stdio.h>
#include<stdlib.h>
int main()
{
	char a[1080];
	char b[1000];
	scanf("%s\n%s",a,b);
	int s=0,m=0;
	int t,y;
	for (int i=0;i<strlen(a);i++)
	{
		m=0;
		if(a[i]==b[i])
		{
			t=i;
			while(a[i]==b[i] && strlen(a))
			{
				i++;
				m++;
			}
		}
		if(s<m)
		{
			s=m;
			y=t;
		}
	} 
	for(;y<strlen(a) && s>0;y++)
	{
		printf("%c",a[y]);
		s--;
	}
}
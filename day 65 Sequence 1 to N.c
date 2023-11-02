/*
The program must accept an integer N as the input. The program generate a sequence of integers from 1 to N. Then the program must replace each integer X in the sequence based on the following conditions.
-If X is a multiple of 3, replace it by Skill
-If X is a multiple of 5, replace it by Rack 
-If X is a multiple of both 3 and 5, replace it by SkillRack
-If X is not divisible of both 3 and 5, keep the integer X as it is.

Boundary Condition(s):
	1 <= N <= 1000

Input Format:
	The first line contains N.

Output Format:
	The N lines contain the sequence based on the given conditions.

Example Input/Output 1:
	Input
		15
	Output:
		1
		2
		Skill
		4
		Rack
		Skill
		7
		8
		Skill
		Rack
		11
		Skill
		13
		14
		SkillRack

Example Input/Output 2:
	Input:
		20
	Output:
		1
		2
		Skill
		Rack
		Skill
		7
		8
		Skill
		Rack
		11
		Skill
		13
		14
		SkillRack
		16
		17
		Skill
		19
		Rack
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n; 
	scanf("%d", &n); 
	int s=1; 
	while(s<=n)
	{
		if(s%3==0 && s%5==0) 
			printf("SkillRack\n");
		else if(s%3==0) 
			printf("Skill\n");
		else if(s%5==0) 
			printf("Rack\n");
		else 
			printf("%d\n",s);
	}
}
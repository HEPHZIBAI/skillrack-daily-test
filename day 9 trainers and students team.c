/*
There are M trainers and N students in a programming training center. The head of the training center wants to form the maximum number of teams to train the students So he has two different criteria which are given below. 
Criteria 1:
	Each team should consist of exactly one trainer and two students. Each trainer and student should belong to exactly one team.

Criteria 2:
	Each team should consist of exactly two trainers and one student. Each trainer and student should belong to exactly one team. The head of the training center wants to know which criteria form the maximum number of teams.

The values of M and N are passed as input to the program. The program must print the output based on the following conditions. If the criteria 1 makes more teams than the criteria 2 then print 1.
	-If the criteria 2 makes more teams than the criteria 1 then print 2. 
	-If both criteria make an equal number of teams then print "ANYONE".

Boundary Condition(s): 
	1 <- M.N <= 10^4

Input Format:
	The first line contains M and N separated by a space.

Output Format:
	The first line contains 1 or 2 or ANYONE.

Example Input/Output 1:
	Input:
		2 6
	Output:
		1
	Explanation:
		There are 2 trainers and 6 students. 
		According to criteria 1, two teams can be formed. 
		According to criteria 2, one team can be formed. 
		Here criteria 1 makes more teams than criteria 2. 
		Hence the output is 1

Example Input/Output 2:
	Input:
		6 4
	Output:
		2

Example Input/Output 3
	Input:
		4 5
	Output:
		ANYONE

*/




#include<stdio.h> 
#include<stdlib.h>

int main()
{
	int m,n;
	scanf("%d%d", &m,&n);
	int m1=m;
	int n1=n;
	int t1=0,t2=0;
	while(m1>0&& n1>1)
	{
		m1--;
		n1-=2;
		t1++;
	}
	m1=m;
	n1=n;
	while (m1>1 && n1>0)
	{
		n1--;
		m1=-2; 
		t2++;
	}
	if(t1>t2)
		printf("1"); 
	else if(t1==t2) 
		printf("ANYONE");
	else
		printf("2");

}
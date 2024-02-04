'''

The program must accept N string values and print the string value that matches the given abbreviation A.

Note: Always only one string will match with the given abbreviation A.

Boundary Condition(s):
	2 <= N, Length of each string <= 100
	1 <=· Length of A <= 50

Input Format:
	The first line contains N.
	The next N lines, each contain a string value.
	The (N+2)nd line contains A.

Output Format:
	The first line contains the string value which matches the abbreviation A.

Example Input/Output 1:
	Input:
		4
		hello Good Morning
		World Health organisation
		World Human Chain
		World War Two
		WHO
	Output:
		World Health organisation
	Explanation:
		Here N = 4.
		In the given 4 string values, the suited string value for the abbreviation
		"WHO" is "World Health organisation".
		Hence the output is World Health organisation

Example Input/Output 2:
	Input:
		4
		hello Good Morning
		World Health Organisation
		World Human Chain
		World War Two
		WWT
	Output:
		World War Two
'''

﻿x=int(input())
star=[]
boy=[]
for i in range(x):
	a=list(input().split())
	boy.append(a)
	t=""
	for j in range(len(a)):
		t+=a[j][0]
	star.append(t.upper())
r=input().strip()
r=r.upper()
for i in range(x):
	if r==star[i]:
		print(*boy[i])
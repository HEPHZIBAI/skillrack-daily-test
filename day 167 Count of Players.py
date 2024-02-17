'''
N players are standing in a line and their country names are passed as the input. If any two adjacent players belong to the same country they are removed from the line. The program must print the final count C of the players who are standing in the line.

Boundary Condition(s):
	1 <= N <= 50
	4 <=Length of each country name <= 50

Input Format:
	The first line contains N.
	The second line contains N country names separated by a space.

Output Format:
	The first line contains C.

Example Input/Output 1:
	Input:
		5
		India Australia India India Australia
	Output:
		1
	Explanation:
		The line contains India Australia India India Australia.
		There are 2 players from India standing nearby.
		So they are removed from the line. Now, the line contains India Australia Australia.
		Again, there are 2 players from Australia standing nearby.
		So they are removed from the line. Now, the line contains India.
		Finally, only one player will remain in the line.
		Hence the output is 1

Example Input/Output 2:
	Input:
		7
		Bangladesh Germany Malaysia Germany Bangladesh Germany Mexico
	Output: 
		7
'''


﻿
n = int(input())
a =list(map(str, input().split()))
flag = 1
while flag == 1:
	s_count = 0
	j=len(a)
	i = 1
	while i < j:
		if a[i]==a[i-1]:
			s_count += 1
			a.pop(i)
			a.pop(i-1)
			j-=2
		i+=1
	if s_count == 0: 
		flag = 0
print(len(a))

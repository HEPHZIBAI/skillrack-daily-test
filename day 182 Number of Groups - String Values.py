'''
The program must accept N string values containing only lower case alphabets as the input. The program must print the number of groups possible among the N string values as the output. The grouping of the string values based on the alphabets that are used to form the string values.

Boundary Condition(s):
	2 <= N <= 100
	1 <= Length of each string <= 100

Input Format:
	The first line contains N.
	The second line contains N string values separated by a space.

Output Format:
	The first line contains the number of aroups possible among the N string values as per the given condition. 

Example Input/Output 1:
	Input:
		6
		dog cat maths tac god act
	Output: 
		3
	Explanation:
		The 3 possible groups are given below.
		Group 1 contains 3 string values: cat, tac and act are formed using the alphabets a, c and t.
		Group 2 contains 2 string values: dog and god are formed using the alphabets d, g and o.
		Group 3 contains 1 string value: maths is formed using the alphabets a, h, m, s and t.
		So 3 is printed as the output.

Example Input/Output 2:
	Input:
		5
		aab aba ab aaab babbb
	Output: 
		1
	Explanation:
		All the 5 string values are formed using the alphabets a and b.
		Here, only one grouping is possible. So 1 is printed as the output.

Example Input/Output 3:
	Input:
		a mask ask as
	Output: 
		4
﻿'''


n = int(input())
S = list(map(str, input().split()))

for st in s:
	key=''.join(sorted(set(st)))
	if key not in g:
		g[key] = 1
	else:
		g[key] += 1
print(len(g))

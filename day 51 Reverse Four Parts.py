'''
The program must accept a string $ where the length of S is always a multiple of 4 as the input. The program must split the string S into four equal parts. Then the program must reverse the characters in each part. Finally, the program must print the modified four equal parts of the string S as the output.

Boundary Condition(s):
	4<= Length of S <= 1000

Input Format:
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input:
		paraacetoaminophenol
	Output
		aarap aotec ponim loneh
	Explanation
		The four equal parts of the string S are parsa cotos minop and henol After reversing the characters in the four parts, they become sarap aotec ponim and longh Hence the output is sarap sotec ponim loneh

Example Input/Output 2:
	Input:
		FAST
	Output
		F A S T
'''


a=input().strip()
h=int(len(a)/4)
i=0
while(h<=len(a)):
	f=a[i:h]
	print (f[::-1], end=" ")
	i=h
	h+=int(len(a)/4)
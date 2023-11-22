'''
The program must accept a string S containing alphabets and digits as the input. For each substring X containing only digits in the string S, the program must replace the substring X by the largest digit in it. Then the program must print the modified string S as the output.

Boundary Condition(s):
	2 <= Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The first line contains the modified string S.

Example Input/Output 1:
	Input:
		abc132sdfg78909okokok3ok
	Output:
		abc3sdfg9okokok3ok
	Explanation:
		In the given string abc132sdfg78909okokok3ok,
		The first substring 132 is replaced by the largest digit 3.
		The second substring 78909 is replaced by the largest digit 9.	
		The third substring 3 has only one digit so keep as it is. So abc3sdfg9okokok3ok is printed as the output.

Example Input/Output 2: 
	Input
		123562A
	Output
		6A
'''

a=input().strip()
i=0
while(i<len(a)):
	while(i<len(a) and a[i].isalpha()): 
		print(a[i], end="") 
		i+=1
	s=0
	while(i<len(a) and a[i].isdigit()): 
		if(s<=int(a[i])): 
			s=int(a[i])
		i+=1
	if(a[i-1].isdigit()): 
		print(s,end="")

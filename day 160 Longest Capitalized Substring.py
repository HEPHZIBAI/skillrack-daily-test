
'''
The program must accept a string $ containing only alphabets as the input. The program must print the longest substring of minimum length 2 in S which contains the first alphabet in upper case and the remaining alphabets in lower case. If more than one such substrings have occurred in S, the program must print the first occurring substring as the output. If there is no such substring, the program must print -1 as the output.

Boundary Condition(s):
	3 <= Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The first line contains the longest substring or -1 as per the given conditions.

Example Input/Output 1:
	Input:
		ThisIsSkillRack
	Output: 
		Skill
	Explanation:
		The longest substring which contains the first alphabet in upper case and the remaining alphabets in lower case is Skill.
		Hence the output is Skill

Example Input/Output 2:
	Input:
		abcdefghijklmnopqrst
	Output:
		Fghi

Example Input/Output 3:
	Input:
		skillRACK
	Output: 
		-1

'''


a=input().strip()
b=""
i=0
l=0
while(i<len(a)):
	f=""
	if a[i].isupper():
		f+=a[i] 
		i+=1
		while(i<len (a) and a[i].islower()):
			f+=a[i]
			i+=1
	else:
		i+=1
	if len(f)>len(b):
		b=f

if len(b)>=2:
	print(b)
else:
	print(-1)

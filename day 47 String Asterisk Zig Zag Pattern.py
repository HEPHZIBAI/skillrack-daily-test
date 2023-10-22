'''
The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	2< Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		abcde
	Output
		abcde
		abcd*
		*bede
		abc**
		**cde
		ab***
		***de
		a****
		****e
		*****
		*****

Example Input/Output 2:
	Input:
		How
	Output
		How
		Ho*
		*OW
		H**
		**w
		***
		***
'''

a=input().strip()
print(a)
for i in range(1,len(a)): 
	print(a[0:len(a)-i], end="")
	for k in range(i): 
		print("*", end "")
	print()
	for k in range(i):
		print("*", end="")
	print (a[i:])
print('*'*(len(a)))
print('*'*(len(a)))
'''
The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	3<= Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		skillrack
	Output:
		skillrack
		kkillrack
		iiillrack
		lllllrack
		lllllrack
		rrrrrrack
		aaaaaaack
		cccccccck
		kkkkkkkkk

Example Input/Output 2:
	Input:
		huge
	Output:
		huge
		uuge
		ggge
		eeee
'''
a=input().strip()
k=1
for i in a:
	print (i*k, end="")
	print (a[k:])
	k+=1
'''
The program must accept a string S with spaces as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s): 
	2 < Length of 5 <= 100

Input Format:
	The first line contains S.

Output Format:
	The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input
	Very Useful One
	Output
	V 
	Ve
	Ver
	Very
	U
	Us 
	Use
	Usef
	Usefu
	Useful
	о
	On
	One

Example Input/Output 2:
	Input:
		skill is power
	Output
		s
		sk
		ski
		skil
		skill
		i
		is
		P 
		po
		pow
		powe
		power
'''


S= input().split()

for i in s:
	x=1
	for l in i: 
		print(l[0:x])
		x+=1
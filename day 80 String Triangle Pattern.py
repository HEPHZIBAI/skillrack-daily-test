'''
The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	3 <= Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The lines containing the desired pattern as shown in the fixample Input/Output section.

Example Input/Output 1:
	Input:
		skillrack
	Output
		s********
		ks*******
		ski******
		liks*****
		skill****
		rlliks***
		skillra**
		carlliks*
		skillrack

Example Input/Output 2:
	Input
		hope
	Output
		h***
		oh**
		hop*
		epoh
'''

a=input().strip()
k=1
for i in range(len(a)): 
	if(i==0 or i%2==0): 
		print(a[0:k], end="")
	else:
		f=a[0:k] 
		print(f[::-1], end="") 
	print('*'*(len(a)-k))
	k+=1
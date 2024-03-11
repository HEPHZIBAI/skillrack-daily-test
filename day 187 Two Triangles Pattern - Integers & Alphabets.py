'''

The program must accept an odd integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	3 <= N <= 999

Input Format:
	The first line contains N.

Output Format:
	The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input: 
		5
	Output: 
		1 * * * * a
		2 3 * * b c
		4 5 6 d e f 
		7 8 * * g h
		9 * * * * i

Example Input/Output 2:
	Input:
		7
	Output: 
		1 * * * * * * a
		2 3 * * * * b c
		4 5 6 * * d e f
		7 8 9 10 g h i j
		11 12 13 * * k l m 
		14 15 * * * * n o
﻿		16 * * * * * * p

Example Input/Output 3:
	Input:
		11
	Output:
		1 * * * * * * * * * * a
		2 3 * * * * * * * * b c 
		4 5 6 * * * * * * d e f
		7 8 9 10 * * * * g h i j
		11 12 13 14 15 * *k l m n o
		16 17 18 19 20 21 p q r s t u
		22 23 24 25 26 * * v w x y z 
		27 28 29 30 * * * * a b c d
		31 32 33 * * * * * * e f g
		34 35 * * * * * * * * h i
		36 * * * * * * * * * * j
'''


a=int(input())
k=1
m='a'
y=a-1
for i in range(0,(a//2)+1): 
	for j in range(i+1):
		print(k,end=" ")
		k+=1
	print("* "*y, end="") 
	for j in range(i+1):
		print(m,end=" ")	
		if m=='z':
			m='a'
		else:
			m=chr(ord (m)+1)
	y-=2
	print()
y=2

for i in range(0,a//2):
	for j in range((a//2)-i): 
		print(k,end=" ")
		k+=1
	print("* "*y,end="") 
	for j in range((a//2)-i):
		print(m,end=" ")
		if m=='z':
			m='a'
		else:
			m=chr(ord (m)+1)
	y+=2﻿
	print()

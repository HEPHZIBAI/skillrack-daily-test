'''
The program must accept a string S containing multiple words as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	3 <=Length of S <= 100

Input Format:
	The first line contains S.

Output Format:
	The first line contains the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		he is a good boy
﻿	Output:
		+--+--+-+----+---+
		|he|is|a|good|boy|
		+--+--+-+----+---+

Example Input/Output 2:
	Input:
		stay home stay safe
	Output:
		+----+----+ ·--+----+
		|stay|home|stay|safe|
		+----+----+----+----+
'''


a=input().split()
print('+',end="")
for i in a:
	print('-'*len(i),end="+")

print('\n',end="")

for i in a:
	print(i,end="|")

print('\n+',end="")

for i in a:
	print('_'*len(i),end="+") 
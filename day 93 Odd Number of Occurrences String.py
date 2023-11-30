'''
The program must accept a string S as the input. The program must print the characters with an odd number of occurrences in the order of their occurrence in S as the output. If there is no such character in the string S then the program must print -1 as the output.

Boundary Condition(s):
	2 <= Length of S <= 1000

Input Format:
	The first line contains S.

Output Format:
	The first line contains the characters with an odd number of occurrences in the order of their occurrence in S.

Example Input/Output 1:
	Input
		nneettwwoorkwo
	Output
		work
	Explanation:
		In the string nneettwwoorkowe, only the four characters w, o, r, and ik have occurred the odd number of times.Hence the outnut is work

Example Input/Output 2:
	Input:
		roboticsrobotics
	Output
		-1

Example Input/Output 3:
	Input
		5#ATES#5#
	Output:
		5#ATE
'''

a=input().strip() 
b=[]
for i in a:
	if i not in b:
		k=a.count(i) 
		if k%2!=0: 
			b.append(i)

for i in b: 
	print(i,end="")

if len(b)==0: 
	print("-1")
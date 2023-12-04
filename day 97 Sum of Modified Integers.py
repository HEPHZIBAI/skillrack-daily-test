'''
The program must accept N integers as the input. The program must remove the first occurrence of 0 in each integer among the N integers. Then the program must print the sum of the N modified integers as the output.

Boundary Condition(s):
	2 <= N <= 100
	10 <= Each integer value <= 10^5

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format:
	The first line contains the sum of the N modified integers.

Example Input/Output 1:
	Input
		3
		100 320 10020
	Output
		1062
	Explanation:
		After removing the first occurrence of 0 in each integer, the three integers become 10, 32 and 1020.
		So their sum 1062 is printed as the output (10 + 32 + 1020 = 1062).

Example Input/Output 2:
	Input
		4
		87 157 10 13
	Output
		258
'''

n=int(input())
a=input().split()
s=0
b=[]
for i in a:
	d=[]
	for j in i:
		d.append(j)
	if('0' in d):
		d.remove('0')
	y=""
	for k in d:
		y+=k
	s+=int(y)
	b.append(d)
print(s)
'''
The program must accept N integers as the input. The program must form a binary representation B by concatenating the last two bits of each integer among the ti integers (left to right). Then the program must print the decimal equivalent of Bas the output.

Boundary Condition(s):
	1 < N <= 31
	2<=Each integer value <= 10^5

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format:
	The first line contains the decimal equivalent of B.

Example Input/Output 1:
	Input 
		4
		7 5 8 2
	Output 
		210
	Explanation:
		The last two bits in the binary representation of 7 is 11. 
		The last two bits in the binary representation of 5 is 01. 
		The last two bits in the binary representation of 8 is 00 
		The last two bits in the binary representation of 2 is 10. 
		So the obtained binary representation B is 11010010 
		The decimal equivalent of 11010010 is 210 
		Hence the output is 210

Example Input/Output 2:
	Input:
		3
		12 10 32
	Output:
		8
'''
a=int(input())
b=input().split()
c=""
k=""
for i in b:
	d=int(i)
	c=""
	while(d>0 and len(c)<2):
		m=d%2
		if(m==1):
			c+='1'
		else:
			c+='0'
		d//=2
	c=c[::-1]
	k+=c
o = len(k) - 1
p=0
f=1
l=0
while(o>=0):
	if(k[o]=='1'):
		l=1
	else:
		l=0
		p+=(f*l)
		f*=2
	o-=1
print(p)
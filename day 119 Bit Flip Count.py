'''
The program must accept two integers A and B as the input. The program must print the number of bits that need to be flipped in the binary representation of A to form B as the output.

Boundary Condition(s): 
	2 <= A, B <= 10^5

Input Format:
	The first line contains A and B separated by a space.

Output Format:
	The first line contains the number of bits that need to be flipped in the binary representation of A to form B.

Example Input/Output 1:
	Input
		5 6
	Output: 
		2
	Explanation:
		The binary representation of 5 is 101.
		The binary representation of 6 is 110.
		After flipping the last 2 bits in the binary representation of 5, it becomes 110. 
		So 2 is printed as the output.

Example Input/Output 2:
	Input
		10 20
	Output
		4
'''
a,b=map(int, input().split())
x=[]
y=[]
h=0
while(a>0):
	m=a%2
	x.insert(0,m)
	a//=2

while(b>0):
	m=b%2
	y.insert(0,m)
	b//=2

while(len(x)<len(y)): 
	x.insert(0,0)

while(len(x)>len(y)): 
	y.insert(0,0)

for i in range(len(x)): 
	if(x[i]=y[i]): 
		h+=1

print(h)





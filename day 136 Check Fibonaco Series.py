'''
The program must accept a string S containing only alphabets as the input. The program must print YES if the frequencies of all the alphabets present in the string S form the Fibonacci series. Else the program miast print NO as the output. Note: Here, the fibonacci series starts with 1 as the frequency of any alphabet in the string S cannot be 0.

Boundary Condition(s): 
	1 <= Length of S <= 10^4

Input Format
	The first line contains S.

Output Format:
	The first line contains YES or NO.

Example Input/Output 1:
	Input
		abbcddd
	Output:
		YES
	Explanation:
		In the string abbcddd, the frequency of the alphabet a is 1. 
		In the string abbcddd, the frequency of the alphabet b is 2. 
		In the string abbeddd, the frequency of the alphabet c is 1. 
		In the string abboddd, the frequency of the alphabet d is 3. 
		The frequencies of the four alphabets form the fibonacci series 1123. 
		Hence the output is YES

Example Input/Output 2:
	Input
		abBc
	Output
		NO

Example Input/Output 3:
	Input
		acAcBcbBcbBc
	Output
		YES
'''


a=input().strip()
b=set(a)
c=[]
d=[]
x=1
y=1
z=x+y

if(len(b)==1):
	d.append(x)
else:
	d.append(x)
	d.append(y)
	while(len(d)<len(b)):
		d.append(z)
		x=y
		y=z
		z=x+y

for i in b:
	h=a.count(i)
	c.append(h)
c.sort()
if(c==d):
	print("YES")
else:
	print("NO")
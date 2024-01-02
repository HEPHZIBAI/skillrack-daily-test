'''
The program must accept N integers as the input. For every two integers and among the N integers, the program must remove the last digit of X and the first digit of Y and form an integer T by concatenating those digits. Then the program must insert the integer T between X and Y. Finally, the program must print the sum of 218 1 integers as shown in the Example Input/Output section.

Boundary Condition(s): 
	2< N < 100 
	100<= Each integer value <= 10^8

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format: 
	The first line contains 2N integer values as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		5
		340 651 2000 3004 853
	Output: 
		34+6+5+12+0+3+0+48 +53 = 161
	Explanation: 
		The given 5 integers are 340, 651, 2000, 3004 and 853. 		After inserting the new integers between every two integers as per the given conditions, the integers become 34, 6, 5, 12,0, 3, 0, 48 and 53. 
		The sum of those integers is 161(34+6+5+12+0+3+0+48+53). 
		Hence the output is 34+6+5+12+0+30+48 +53 = 161

Example Input/Output 2:
	Input:
		3 
		60646 157 5878
	Output 
		6064+61+5+75 +878 = 7083

Example Input/Output 3:
	Input:
		4
	Output 
		10+1+0+1+0+1+0=13
'''

n=int(input())
a=list(input().split())
b=[]
s=0

for i in range(n-1):
	x=a[i]
	y=a[i+1]
	a[i]=x[:len(x)-1]
	a[i+1]=y[1:]
	f=x[len(x)-1]+y[0]
	b.append(f)

for i in range(0,n-1):
	h=int(a[i])
	l=int(b[1])
	print(h, "+",1,"+", end=" ")
	s+=h

for i in b:
	h=int(i)
	s+=h

k=int(a[n-1])
s+=k
print(k,"=",s,end="")
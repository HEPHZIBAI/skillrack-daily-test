'''
The program must accept an integer N as the input. The program must form the largest integer X by removing exactly one digit from the last three digits of N. Then the program must print the integer X as the output.

Boundary Condition(s): 
	100 <- N<= 10^8

Input Format:
	The first line contains N.

Output Format: 
	The first line contains X.

Example Input/Output 1:
	Input 
		15742
	Output:
		1574
	Explanation:
		If the unit digit 2 is removed, the integer becomes 1574. If the tenth digit 4 is removed, the integer becomes 1572. If the hundredth digit 7 is removed, the integer becomes 1542.Among these three integers, the largest integer is 1574. Hence the output is 1574

Example Input/Output 2:
	Input 
		6108
	Output 
		618
'''

n=input()
l=[]

for i in range(len(n)-1,len(n)-4,-1): 
	l.append(int(n[:i]+n[i+1:])) 
print(max(l))
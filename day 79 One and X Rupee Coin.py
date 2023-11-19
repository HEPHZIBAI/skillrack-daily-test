'''
A boy has M 1 rupee coins and NX rupee coins. He needs to pay a bill of K rupees. The values of X, M, N and K are passed as input to the program. The program must print YES if it is possible to pay exactly K rupees from the M 1 rupee coins and the N X rupee coins. Else the program must print NO as the output.

Boundary Condition(s):
	2 <= x <= 10
	1 <= M, N <= 100
	3 <= K <=1000

Input Format:
	The first line contains X, M, N and K each separated by a space.

Output Format:
	The first line contains YES or NO based on the given condition.

Example Input/Output 1:
	Input 
		2 6 5 13
	Output 
		YES
	Explanation
		In the given integers 2 65 13, there are six 1 rupee coins and five 2 rupee coins. From that the sum of five 2 rupee coins (5 X 2 = 10) and three 1 rupee coins (3 X 1 = 3) is 13.So YES is printed as the output.

Example Input/Output 2:
	Input
		3 1 8 14
	Output
		NO
'''
x,a,y,b=map(int,input().split()) 
t=(x*y)+a
if(t>=b and (b%y)<=a): 
	print("YES")
else: 
	print("NO")
'''
The program must accept a list of integers containing all the divisors of X and all the divisors of Y (X and Y are two positive integers where X >= Y). The program must find the integers X and Y from the given list of divisors and print them as the output.

Boundary Condition(s): 
	1 < Each integer value <= 10^4

Input Format:
	The first line contains a list of integers separated by a space.

Output Format:
	The first line contains X and Y separated by a space.

Example Input/Output 1: 
	Input: 
		10 2 8 1 2 4 1 20 4 5
	Output: 
		20 8
	Explanation:
		The factors of 20 are 1 2 4 5 10 and 20.
		The factors of 8 are 1 2 4 and 8. So, all the factors of 20 and 8 have occurred in the given list of integers.
		Hence the output is 20 8

Example Input/Output 2:
	Input
		1 2 3 6 1 2 3 6
	Output
		6 6
'''


m=list(map(int, input().split())); 
k=max(); 
p,1k=[], []
for i in m:
	if max(m)%i and i not in p:
		p.append(1)
	else:
		lk.append(i)
print(max(p),max(1k))
'''
The program must accept two prime integers X and Y as the input. The program must print the most repeated digit in the prime integers from X to Y. If more than one digit has repeated the maximum number of times then the program must print the largest digit among those digits as the output.

Boundary Condition(s): 
	2 <= x < Y <= 10^8

Input Format:
	The first line contains X and Y separated by a space.

Output Format:
	The first line contains the most repeated digit in the prime integers from X to Y.

Example Input/Output 1:
	Input: 
		2 11
	Output: 
		1
	Explanation:
		The prime integers from 2 to 11 are 2, 3, 5, 7 and 11.
		The frequency of the digit 1 is 2.
		The frequency of the digit 2 is 1.
		The frequency of the digit 3 is 1.
		The frequency of the digit 5 is 1. 	
		The frequency of the digit 7 is 1. 
		Here the most repeated digit is 1, so 1 is printed as the output.

Example Input/Output 2:
	Input:
		17 29
	Output: 
		9
'''

def check(n):
	if n < 2:
		return 0
	for i in range(2, int(n**0.5) + 1):
		if n%i==0:
			return 0
	return 1


x, y = map(int, input().split())
dc=[0]*10
for num in range(x, y+1):
	if check(num):
		for d in str(num):
			dc[int(d)] += 1
	mc = max(dc)
	mrd = max([i for i, c in enumerate(dc) if c == mc]) 
print(mrd)
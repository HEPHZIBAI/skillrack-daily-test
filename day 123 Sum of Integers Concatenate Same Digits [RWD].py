'''
The program must accept N integers as the input. The program must print the sum of integers that are formed by concatenating the digits of the same value among the digits of N integers as the output.

Boundary Condition(s): 
	1 <= N <= 50 
	1 <= Each integer value <= 10^5

Input Format:
	The first line contains N. 
	The second line contains N integers separated by a space.

Output Format:
	The first line contains the sum of integers as per the given condition.

Example Input/Output 1:
	Input:
		4 
		3 45 332 654
	Output: 
		440
	Explanation:
		Here the given 4 integers are 3. 45. 332 and 654.
		The integers that are formed by concatenating the digits of the same value are 2, 333, 44, 55 and 6.
		The sum of those integers is 440 (2+333+44+55+6=440). So 440 is printed as the output

Example Input/Output 2:
	Input
		5
		986 12641 3218 1800 40
	Output 
		2143
'''
import re
input()
x="".join(sorted("".join(input().split()))) 
print(sum([int(i) for i in re.findall('+1+12+ 3+ 4+ 5+ 6+ 7+ 8+ 9+',x)]))
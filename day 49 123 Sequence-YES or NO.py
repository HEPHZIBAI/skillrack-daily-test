'''
The program must accept N integers as the input. The program must print YES if the sequence 123 has occurred in the N integers. Else the program must print NO as the output.

Boundary Condition(s):
	3 <= N <= 100
	1 < Each integer value <= 3

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format:
	The first line contains YES or NO.

Example Input/Output 1:
	Input
		5
		1 1 2 3 1
	Output
		YES
	Explanation
		The sequence 123 has occurred in the given 5 integers. So YES is printed as the output.

Example Input/Output 2:
	Input
		6
		1 2 1 2 1 3
	Output
		NO
'''
a=int(input())
b=input().strip()
d=b.count("1 2 3")
if(d):
	print("YES")
else:
	print("NO")
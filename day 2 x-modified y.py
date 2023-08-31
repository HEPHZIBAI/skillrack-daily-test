'''
The program must accept an integer X as the input. The program must form the minimum possible integer Y by modifying the integer X based on the following conditions.
-Any digit D in X (at most all the digits) can be replaced by 9-D (9 minus D). Y should not contain leading zeros.

-The number of digits in X and Y should be equal.

Finally, the program must print the integer Y as the output.

Boundary Condition(s):
	1 <= X <= 10^7
Input Format: 
	The first line contains X.
Output Format:
	The first line contains Y.

Example Input/Output 1:
	Input
		27
	Output 
		22
	Explanation:
		The minimum possible integer is 22 which is obtained by replacing the digit 7 with 2 (9-7).
	Hence the output is 22

Example Input/Output 2:
	Input
		4545
	Output
		4444
'''



s=input().strip()
a=[None for _ in range(len(s))] 
k=0
for i in range(len(s)):
	if i==k and int(s[i])==9: 
		a[i]=s[i]
	else:
		if 9-int(s[i])<=int(s[i]): 
			a[i]=str(9-int(s[i]))
		else:
			a[i]=s[i]
print(int("".join(a)))
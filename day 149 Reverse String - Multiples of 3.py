'''

The program must accept a string S containing only alphabets as the input. The program must reverse the string S. Then the program must print the alphabets which are present at the positions of multiples of 3 in the modified string as the output.

Boundary Condition(s):
	3 <= Length of S <= 1000

Input Format:
	The first line contains S.
Output Format:
	The first line contains the alphabets as per the given condition.

Example Input/Output 1:
	Input:
		embezzling
	Output:
		izm
	Explanation:
		After reversing the string embezzling, the string becomes gnilzzebme.
		In the string gnilzzebme, the alphabets present at the positions of multiples of 3 are i, z and m.
		Hence the output is izm

Example Input/Output 2:
	Input:
		Nature
	Output: 
		uN
'''

a=input().strip()
a=a[::-1]
for i in range(len(a)): 
	if (i+1)%3==0:
		print(a[i], end="")

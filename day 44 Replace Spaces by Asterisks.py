'''

The program must accept a string S with spaces as the input. The program must replace all the spaces by (asterisk) in the string S. Then the program must bring all the asterisks to the end of the string S. Finally, the program must print the modified string S as the output.

Boundary Condition(s): 
	3< Length of S <= 1000
Input Format:
	The first line contains S.

Output Format:
	The first line contains the modified S.

Example Input/Output 1:
	Input:
		Handle with care
	Output
		Handlewithcare***
	Explanation:
		After replacing all the spaces by in the string Handle with care, Handle with care After bringing all the asterisks to the end of the string, it becomes Handlewithcare"*
Hence the output is Handlewithcare**

Example Input/Output 2:
	Input: 
		of the people by the people for the people
	Output:
		ofthepeoplebythepeopleforthepeople*******
'''
a-input().strip()
b=a.count(" ") 
a=a.split()
for i in a:
	print(i,end="")
for i in range(b): 
	print("*", end="')
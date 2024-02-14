'''
The program must accept an integer N as the input. For each digit D in N, the program must form an integer by concatenating all the digits from D to 0 in the reverse order. Then the program must print the sum of integers which are formed from the digits of N as the output.

Boundary Condition(s):
	1 <= N <= 10^5

Input Format:
	The first line contains N.

Output Format:
	The first line contains the sum of integers which are formed from the digits of N.

Example Input/Output 1:
	Input:
		4052
	Output: 
		586630
	Explanation:
		N = 4052
		43210 + 0 + 543210 + 210 = 586630

Example Input/Output 2:
	Input:
		913
	Output:
		9876546430
'''



def jp(x): 
	x=int(x) 
	t=""
	for i in range(x+1): 
		t+=str(i)
	return t[::-1]

x=input().strip()
jan=[]
for i in range(len(x)):
	jan.append(int(jp(x[i])))
print(sum(jan))

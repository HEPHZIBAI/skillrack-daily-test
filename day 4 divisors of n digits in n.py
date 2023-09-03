'''
The program must accept an integer N as the input. The program must find all the combinations of the digits in the integer N. Then the program must print the combinations which are the factors of N in ascending order as the output. If there is no such combination then the program must print-1 as the output. 
Note: Exclude 1 and N from the factors of N.

Boundary Condition(s): 1 <= N < 999999999

Input Format:
	The first line contains N.

Output Format:
	The lines each contain an integer or the first line contains-1.

Example Input/Output 1:
	Input 
		12345
	
	Output
		3
		5 
		15
	Explanation:
		The integer N (12345) is divisible by 3, 5 and 15 which are all the combinations of the digits in the integer 12345. 35 15 are already in sorted order.So the output is 35 15

Example Input/Output 2:
	Input 
		21
	
	Output
		-1
'''



#answer




s=input().strip()
k=[]
def gas(A,B):
	if(len(A)==0):
		if(Bl=""): 
			k.append(int(B))
		return 
	gas(A[1:],B+A[0]) 
	gas (A[1:],B)

gas(s,' ') 
k.sort()
p=0
for i in range(len(k)): 
	if(k[i]!=0 and int(S)%k[i]==0 and k[i] not in (1,int(S))): 
		print(k[i])
		p=1
if(p==0):
	print(-1)


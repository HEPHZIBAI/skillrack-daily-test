'''

The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
	2 <= N <= 100
Input Format:
	The first line contains N.

Output Format:
	The lines contain the desired pattern as shown in the Example
Input/Output section.

Example Input/Output 1:
	Input:
		3
	Output:
		3333
		4414
		5525
		6636
		3333

Example Input/Output 2:
	Input:
		4
	Output:
		44444
		55515
		66626
		77737
		88848
		44444

'''


a=int(input())
b=str(a)*(a+1)
c=a+1

print(b)

for i in range(a):
	h=str(c)*(a-1)
	print(h,end="")
	print(i+1,c,sep="")
	c+=1

print(b)

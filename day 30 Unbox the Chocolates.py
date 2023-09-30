'''
A girl has N boxes of chocolates. The number of chocolates in each box is passed as input. She wants to eat K chocolates from the N boxes based on the following conditions

-She must open the boxes in the given order. - She can't open more than one box in a day.
-Every day she can eat at most 8 chocolates. (If a box contains more than 8 chocolates, she can eat the remaining chocolates later)

The value of K is also passed as the input to the program. The program must print the minimum number of days she has to eat exactly K chocolates as the output. Note: The value of K is always less than or equal to the total number of chocolates in the N boxes.

Boundary Condition(s):
	1 <= N <= 100
	1< K, Each integer value <=1000

Input Format:
	The first line contains N and K separated by a space. The second line contains N integers separated by a space.

Output Format:
	The first line contains the minimum number of days she has to eat exactly K chocolates.

Example Input/Output 1:
	Input 
		3 18
		10 10 10
	Output
		3
	Explanation:
		On the first day, she can eat 8 chocolates from the first box (2 chocolates are remaining in the first box).
		On the second day, she can eat 2 chocolates from the first box and 6 chocolates from the second box (4 chocolates are remaining in the second box). On the third day, she can eat 2 chocolates from the second box. 
		The third box is not opened as she can get 18 chocolates from the first 2 boxes. So it takes 3 days to eat 18 chocolates.
		Hence the output is 3

Example Input/Output 2:
	Input
		2 3
		1 2
	Output
		2

Example Input/Output 3:
	Input
		4 15 
		5 10 4 7
	Output
		3
'''


a, k=map(int, input().split()) 
ll=list (map(int, input().split()))
l=l1
c=0;i=0;d=0
n=l[i] 
while c<k:
	if n<=8:
		c+=n
		n=0
	else:
		c+=8 
		n-=8
	i+=1
	if i<len(l1): 
		n+=l[i]
	d+=1
print(d)
'''
The program must accept N integers as the input. The program must form an integer X so that each digit in X must have the maximum value in its place value among the N integers. Finally, the program must print the integer X as the output.

Note: The place values are nothing but ones, tens, hundreds, thousands and so on.

Boundary Condition(s):
	2 <= N <= 1000 
	0 <= Each integer value <= 10^8

Input Format:
	The first line contains N.
	The second line contains N integers separated by a space.

Output Format:
	The first line contains X

Example Input/Output 1:
	Input
		4
		8 73 2134 5736
	Output: 
		5778
	Explanation:
		The maximum unit digit among the unit digits of 8, 73, 2134 and 5736 is 8
		The maximum tenth digit among the tenth digits of 8, 73, 2134 and 5736 is 7
		The maximum hundredth digit among the hundredth digits of 8, 73, 2134 and 5736 is 7
		The maximum thousandth digit among the thousandth digits of 8, 73, 2134 and 5736 is 8
		Hence the output is 5778

Example Input/Output 2:
	Input:
		5 
		8008 102 709 900 924901
	Output: 
		928909

Example Input/Output 3:
	Input:
		6
		275 375 475 575 675 875
	Output:
		875

'''
n = int(input())

arr = list(map(int,input().split()))

m = max(arr)

ans = [0]*(len(str(m)))

for i in arr:

ind = 0

while(i>0):

c = 1%10

ans[ind] = max(int(ans[ind]),c)

ans[ind] = str(ans[ind])

i =1//10

ind += 1

ans.join(ans)

print(int(ans[::-1]))
/*
The program must accept an integer N as the input. The program must print the maximum possible integer which is formed by removing exactly one bit from the binary representation of N as the output.

Boundary Condition(s): 
	2 <= N <= 2^31

Input Format:
	The first line contains N.

Output Format:
	The first line contains the maximum possible integer which is formed by removing exactly one bit from the binary representation of N.

Example Input/Output 1:
	Input: 
		5
	Output: 
		3
	Explanation:
		The binary representation of 5 is 101.
		All possible combinations after removing exactly one bit from 101 are given below. 
		The decimal equivalent of 10 is 2.
		The decimal equivalent of 11 is 3.
		The decimal equivalent of 01 is 1.
		Here the maximum integer value is 3, so it is printed as the output.

Example Input/Output 2:
	Input
		31
	Output:
		15
*/

import java.util.*;
public class Hello
{
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		String s = Integer.toBinaryString(sc.nextInt()), t = ";
		int n,c = 0;
		for(int i=0;i<s.length();i++) 
		{
			t=s.substring(0,1)+s.substring(i+1,s.length());
			c = Integer.parseInt(t, 2); 
			if(c>n) 
				n = c;
		}
		System.out.print(n);
	}
}
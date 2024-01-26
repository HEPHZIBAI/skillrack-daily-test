/*
program must accept two integers M and N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Note: N is always odd.

Boundary Condition(s):
	0 <= M <= 9
	5 <= N <= 99

Input Format:
	The first line contains M and N separated by a space.

Output Format:
	The first N lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
	Input:
		1 7
	Output: 
		******1
		******1
		******1
		******1
		******1
		******1
		******1

Example Input/Output 2:
	Input:
		5 5
	Output:
		55555
		5****
		55555
		****5
		55555

Example Input/Output 3:
	Input:
		2 7
	Output:
		2222222
		******2
		******2
		2222222
		2******
		2******
		2222222
*/




﻿import java.util.*;

public class Hello 
{
	static void zero(int n) 
	{
		for(int i=0;i<n;i++) 
		{
			for(int j=0;j<n;j++) 
			{
				if(i==0 || j==0 || i==n-1 || j==n-1) 					System.out.print(0); 
				else 
					System.out.print('*');
			} 
			System.out.println();
		}
	}
	
	static void one(int n) 
	{
		for(int i=0;i<n;i++) 
		{	
			System.out.println("*".repeat(n-1)+"1");
		}
	}
	
	static void two(int n) 
	{
		System.out.println("2".repeat(n));
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("".repeat(n-1)+"2"); 			System.out.println("2".repeat(n)); 
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("2"+"".repeat(n-1));
		System.out.println("2".repeat(n));
	}

	static void three(int n) 
	{
		System.out.println("3".repeat(n)); 
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("".repeat(n-1)+"3"); 		System.out.println("3".repeat(n)):
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("".repeat(n-1)+"3"); 		System.out.println("3".repeat(n));
	}

	static void four(int n) 
	{
		for(int i=0;i<n/2;i++)
			System.out.println("4"+"".repeat(n-2)+"4");
		System.out.println("4".repeat(n));
		for(int i=0;i<n/2;i++)
			System.out.println("* .repeat(n-1)+"4");
	}

	static void five(int n) 
	{	
		System.out.println("5".repeat(n)); 
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("5"+"".repeat(n-1)); 		System.out.println("5".repeat(n)); 
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("".repeat(n-1)+"5"); 		System.out.println("5".repeat(n));
	}

	static void six(int n) 
	{
		System.out.println("6".repeat(n)); 
		for(int i=0;i<(n-3)/2;i++) 						System.out.println("6"+"".repeat (n-1)); 		System.out.println("6".repeat(n));
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("6"+"".repeat(n-2)+"6");
		System.out.println("6".repeat(n));
	}

	static void seven (int n) 
	{
		System.out.println("7".repeat(n)); 
		for(int i=0;i<n-1;i++)
			System.out.println("7".repeat(n-1)+"7");
	}

	static void eight(int n) 
	{
		System.out.println("8".repeat(n));
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("8"+"".repeat(n-2)+"8");
		System.out.println("8".repeat(n)); 
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("8"+"".repeat(n-2)+"8");
		System.out.println("8".repeat(n));
	}

	static void nine(int n) 
	{
		System.out.println("9".repeat(n));
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("9"+"".repeat(n-2)+"9");
		System.out.println("9".repeat(n));
		for(int i=0;i<(n-3)/2;i++)
			System.out.println("".repeat(n-1)+"9"):
		System.out.println("9".repeat(n));
	}

	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in); 
		int m = sc.nextInt(),n =sc.nextInt();
		switch(m) 
		{
			case 0:
				zero(n);
				break;
			case 1:
				one(n);
				break;
			case 2:
				two(n);
				break;
			case 3:
				three(n);
				break;
			case 4:
				four (n); 
				break;
			case 5:
				five(n);
				break;
			case 6:
				six(n);
				break;
			case 7:
				seven(n);
				break;
			case 8:
				eight(n);
				break;
			case 9:
				nine(n);
				break;
		}
	}
}
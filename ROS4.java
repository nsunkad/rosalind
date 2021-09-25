/* 
@author: Nitya Sunkad

PROBLEM 4: Rabbits and Recurrence Relations

*** Given: Positive integers n≤40 and k≤5.

*** Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
*/

import java.util.Scanner;

class Main {

  public static double numRabbitPairs(double n, double k)
  {
    if(n==1)
    {
      return 1.0;
    }
    
    double temp=0.0;
    double totalRabbits = 1.0;
    double numAdults = 0.0;
    for(int i=1; i<=n;i++)
    {
      temp = numAdults;
      numAdults=totalRabbits;
      totalRabbits += temp*k;
    }

    return totalRabbits;
  }
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a value of n (number of months): ");
    int n = sc.nextInt();
    System.out.print("Enter a value of k (number of offspring per litter): ");
    int k = sc.nextInt(); 
    System.out.println("The number of rabbit pairs in month "+n+" is "+numRabbitPairs(n,k));
  }
}

// helpful information: 
//A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if Fn represents the number of rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

//When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

/* 
@author: Nitya Sunkad

PROBLEM 3: Complementing a Strand of DNA

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

*** Given: A DNA string s of length at most 1000 bp.

*** Return: The reverse complement sc of s.
*/

import java.util.Scanner;

class Main {

  public static String reverse(String DNA) //reverses the characters in the DNA string
  {
    String s = "";
    for(int i=DNA.length()-1; i>=0;i--)
    {
      s+=DNA.substring(i,i+1);
    }
    return s;
  }
  public static String reverseComplement(String DNA) //receives a DNA string and returns the complement string (complement: A switched with T, C switched with G, vice versa )
  {
    String str = reverse(DNA);
    String newStr = "";
   for(int i=0; i<str.length();i++)
   {
     if(str.substring(i,i+1).equals("A"))
      newStr+="T";
     else if(str.substring(i,i+1).equals("T"))
      newStr+="A";
     else if(str.substring(i,i+1).equals("C"))
      newStr+="G";
     else if(str.substring(i,i+1).equals("G"))
      newStr+="C";
   }
   return newStr;
  }

  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a DNA string (ex: GATTACA): ");
    String s = sc.next();
    System.out.print("The reverse complement of the input DNA string is: "+reverseComplement(s));
  }
}

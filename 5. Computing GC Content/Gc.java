/* 
@author: Nitya Sunkad

(Just run this one, no user input needed because the program is reading a file)

PROBLEM 5: Computing GC Content

*** Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

*** Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
*/
import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;

class Main {

  public static double getGCContent(String str)
  {
    double gc = 0.0;
    int total =0;
    for(int i=0; i<str.length();i++)
    {
      total++;
      if(str.substring(i,i+1).equals("G") || str.substring(i,i+1).equals("C"))
        gc++;
    }
    return (double)(gc/total)* 100;
  }
  public static int highestInd(ArrayList<String> arr)
  {
    int highest = 0;
    for(int i=0; i<arr.size();i++)
    {
      if(getGCContent(arr.get(i)) > getGCContent(arr.get(highest)))
        highest = i;
    }
    return highest;
  }

  public static void main(String[] args)
  {
    ArrayList<String> fasta = new ArrayList<String>(); // arraylist with FASTA sequences

    ArrayList<String> code = new ArrayList<String>(); // arraylist with DNA sequences

    try
    {
      File dna = new File("fastafile.txt");
      Scanner sc = new Scanner(dna); //reads the dataset FASTA file
      String line;
      String val="";
      while(sc.hasNextLine())
      {
        line = sc.nextLine();
        if(line.substring(0,1).equals(">"))
        {
          code.add(val);
          val = "";
          fasta.add(line);
        }
        else
        {
          val+=line;
        }
      }
      if(val!="")
        code.add(val);

      code.remove(0);

      int i = highestInd(code);
      System.out.println(fasta.get(i));
      System.out.println(getGCContent(code.get(i)));

      //prints the FASTA ID of the DNA code with the highest GC-content

      //prints the DNA code with the highest GC-content 

      //highest GC-content DNA:
      // code.remove(0);
      // System.out.println(fasta);
      // ArrayList<String> a = new ArrayList<String>();
      // a.add("CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG");
      // a.add("CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC");
      // a.add("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT");
      // System.out.println(highestInd(a));

      // System.out.println(fasta.get(highestGCContentIndex(fasta)));
      // System.out.println(code.get(highestGCContentIndex(fasta)));
    }
    catch(Exception e)
    {
      System.out.println(e);
    }
      // System.out.println(highestGCContentIndex(a));
      // // int ind = highestGCContentIndex(fasta);
      // // System.out.println("FASTA ID: "+ fasta.get(ind));
      // // System.out.println("GC-Content: "+ getGCContent(code.get(ind)));
    
  }


  }




// helpful information: The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

//DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

//In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

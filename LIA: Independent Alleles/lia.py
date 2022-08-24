# LIA: Independent Alleles (Mendel's Second Law)
# Source: https://rosalind.info/problems/lia/
from math import comb

# calculates probability of having at least n hybrid offspring in generation k of dihybrid cross
def binomial_prob(k, n):
  sum = 0
  for i in range(n):
    sum += comb((2**k), i) * ((0.25)**(i)) * ((0.75)**((2**k) - i))
  return 1 - sum

# parse input and write probability to output
with open('input.txt','r') as input_file:
  data = input_file.readline().split()
  with open('output.txt','w') as output_file:
    output_file.write(str(binomial_prob(int(data[0]), int(data[1]))))
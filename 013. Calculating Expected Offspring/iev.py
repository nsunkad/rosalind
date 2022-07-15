# IEV: Calculating Expected Offspring
# Source: https://rosalind.info/problems/iev/

""" Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

"""

# parse input and write probability to output
with open('input.txt', 'r') as input_file:
  a, b, c, d, e, f = [int(x) for x in next(input_file).split()]
  with open('output.txt','w') as output_file:
    output_file.write(f'{(4*a + 4*b + 4*c + 3*d + 2*e)/(4* (a + b + c + d + e + f)) * 2 * (a + b + c + d + e + f)}')
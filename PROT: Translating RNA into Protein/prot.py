# PROT: Translating RNA into Protein
# Source: https://rosalind.info/problems/prot/

""" Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""

# store mRNA codon mapping in dict
codons_file = open('codon-table.txt', 'r')
codon_mapping = dict()
codon_table_line = codons_file.readline()
while codon_table_line:
  line = codon_table_line.split()
  for i in range(0, len(line), 2):
    codon_mapping[line[i]] = line[i + 1]
  codon_table_line = codons_file.readline()

# read mRNA input
input_file = open('input.txt', 'r')
mrna = input_file.read()
input_file.close()

# convert mRNA sequence to amino acid sequence
prot = ''
for i in range(0, len(mrna), 3):
  codon = codon_mapping[mrna[i : i + 3]]
  if codon != 'Stop':
    prot += codon
  else:
    break

# write amino acid sequence to output
output_file = open('output.txt', 'w')
output_file.write(f'{prot}')
output_file.close()
                  


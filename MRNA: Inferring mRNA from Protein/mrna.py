# MRNA: Inferring mRNA from Protein
# Source: https://rosalind.info/problems/lia/

# store mRNA amino acid to codon mapping in dict
codons_file = open('codon-table.txt', 'r')
codon_mapping = dict()
codon_table_line = codons_file.readline()
while codon_table_line:
  line = codon_table_line.split()
  for i in range(0, len(line), 2):
    if line[i + 1] in codon_mapping:
      codon_mapping[line[i + 1]].append(line[i])
    else:  
      codon_mapping[line[i + 1]] = [line[i]]
  codon_table_line = codons_file.readline()
codons_file.close()

# calculates # of possibilities for mRNA source strand given amino acid sequence (i.e. reversing translation) mod one million
def reverse_engineer_translation(prot):
  MODULO_CONST = 1000000
  poss = 1
  for char in prot:
    poss *= len(codon_mapping[char])
  return (poss * len(codon_mapping['Stop'])) % MODULO_CONST

with open('input.txt', 'r') as input_file:
  data = input_file.read().replace('\n','')
  with open('output.txt', 'w') as output_file:
    output_file.write(str(reverse_engineer_translation(data)))
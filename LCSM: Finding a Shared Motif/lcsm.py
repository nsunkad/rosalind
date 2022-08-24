# LCSM: Finding a Shared Motif
# Source: https://rosalind.info/problems/lcsm/

""" Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

# parse FASTA-formatted input
dna_strs = []
with open('input.txt', 'r') as input_file:
  FASTA_SIGNATURE_LENGTH = 14
  fasta_dna = input_file.read()
  raw_arr = fasta_dna.split('>')
  for raw in raw_arr:
    r = raw[FASTA_SIGNATURE_LENGTH:].replace('\n','')
    dna_strs.append(r)
  dna_strs.pop(0)
  
# identify shortest DNA strand and remove from dna_strs
smallest = dna_strs[0]
for i in range(len(dna_strs)):
  if len(dna_strs[i]) < len(smallest):
    smallest = dna_strs[i]
dna_strs.remove(smallest)

# checks if passed substring occurs in all indices of list
def strOccursEverywhere(s):
  for str in dna_strs:
    if s not in str:
      return False
  return True

# iterate through bases of smallest to find longest common substring
longest_common_substr = ''
longest_len = 1
while (len(smallest) > 0):
  # print(longest_common_substr)
  if strOccursEverywhere(smallest[:longest_len]):
    if (len(smallest) <= len(longest_common_substr)):
      break
    if (len(smallest[:longest_len]) > len(longest_common_substr)):
      longest_common_substr = smallest[:longest_len]
      longest_len += 1
  else:
    smallest = smallest[1:]
    
with open('output.txt','w') as output_file:
  output_file.write(longest_common_substr)
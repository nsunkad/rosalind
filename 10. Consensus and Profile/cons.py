# CONS: Consensus and Profile
# Application: Finding a Most Likely Common Ancestor
# Source: https://rosalind.info/problems/subs/

""" Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""
import numpy as np

# read dna strings from input
input_file = open('input.txt','r')
all_lines = input_file.read().split('\n')
curr_dna_str = ''
dna_strs = []

for line in all_lines:
  if line[0] != '>':
    line = line.replace('\n', '')
    curr_dna_str += line
  else:
    dna_strs.append(list(curr_dna_str))
    curr_dna_str = ''
dna_strs.append(list(curr_dna_str))
dna_strs.pop(0)

# transpose input to read columns efficiently
dna_strs_transpose = np.array([dna_strs], dtype=object).T
a_list = []
c_list = []
g_list = []
t_list = []

# print(dna_strs_transpose)
# construct profile matrix
for i in range(len(dna_strs_transpose)):
  a_list.append(np.count_nonzero(dna_strs_transpose[i] == 'A'))
  c_list.append(np.count_nonzero(dna_strs_transpose[i] == 'C'))
  g_list.append(np.count_nonzero(dna_strs_transpose[i] == 'G'))
  t_list.append(np.count_nonzero(dna_strs_transpose[i] == 'T'))

profile_matrix = np.array([a_list, c_list, g_list, t_list])
# print(profile_matrix)

# construct consensus string (average case strand) and write to output
output_file = open('output.txt', 'w')
consensus_dict = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

for i in range(len(profile_matrix.T)):
  index_max = np.argmax(profile_matrix.T[i])
  output_file.write(consensus_dict[index_max])

# write profile matrix to output
output_file.write('\n' + 'A: ' + ' '.join(str(v) for v in a_list))
output_file.write('\n' + 'C: ' + ' '.join(str(v) for v in c_list))
output_file.write('\n' + 'G: ' + ' '.join(str(v) for v in g_list))
output_file.write('\n' + 'T: ' + ' '.join(str(v) for v in t_list))
  
output_file.close()

# SUBS: Finding a Motif in DNA
# Source: https://rosalind.info/problems/subs/

""" Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""
# read DNA strs from input file
input_file = open('input.txt', 'r')
dna_s = input_file.readline()
dna_t = input_file.readline()
input_file.close()

# note this problem uses 1-indexing
output_file = open('output.txt', 'w')

# write locations of motif to output file
def motif_locations(s, t):
  orig_s = s
  bases_sheared = 0
  while (t in s):
    output_file.write(f'{s.find(t) + bases_sheared + 1}')
    output_file.write(' ')
    s = s[s.find(t) + 1:]
    bases_sheared = len(orig_s) - len(s)

motif_locations(dna_s, dna_t)
output_file.close()
    

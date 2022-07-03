# IPRB: Mendel's First Law
# Source: https://rosalind.info/problems/iprb/ 

""" Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals 
are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant 
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

def probability_dom_allele(k, m, n):
    prob_n_cross_n_rec = (n / (k + m + n)) * ((n - 1) / (k + m + n - 1)) * 1
    prob_m_cross_n_rec = (n / (k + m + n)) * (m / (k + m + n - 1)) * 0.5
    prob_m_cross_m_rec = (m / (k + m + n)) * ((m - 1) / (k + m + n - 1)) * 0.25
    prob_homozygous_recessive = prob_n_cross_n_rec + prob_m_cross_n_rec + prob_m_cross_n_rec + prob_m_cross_m_rec
    return 1 - prob_homozygous_recessive


input_file = open("input.txt", "r")
data = input_file.readline().split()
result = probability_dom_allele(int(data[0]), int(data[1]), int(data[2]))
input_file.close()

output_file = open("output.txt", "w")
output_file.write(f"{result}")
output_file.close()

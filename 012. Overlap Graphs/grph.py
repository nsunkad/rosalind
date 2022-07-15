# GRPH: Overlap Graphs
# Source: https://rosalind.info/problems/grph/

""" Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

# linked list implementation for true adjacency list

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
class SLL:
  def __init__(self, head):
    self.head = head
  def add_node(self, value):
    if self.head is None:
      self.head = Node(value)
    else:
      curr = self.head
      while curr.next:
        curr = curr.next
      curr.next = Node(value)
      
adjacency_list = []
fasta_ids = []
dnastrs = []

# parse FASTA input
with open('input.txt', 'r') as input_file:
  data_str = input_file.read()
  data = data_str.split('>')
  data.pop(0)
  for item in data:
    item = item.replace('\n', '*',1).replace('\n','')
    fasta_ids.append(item.split('*')[0])
    dnastrs.append(item.split('*')[1])

# set desired overlap length
OVERLAP_LENGTH = 3

# construct adjacency list
for str1 in dnastrs:
  for str2 in dnastrs:
    if str1 == str2:
      continue
    if str1[len(str1) - OVERLAP_LENGTH:] == str2[:OVERLAP_LENGTH]:
      new_SLL = SLL(Node(fasta_ids[dnastrs.index(str1)]))
      new_SLL.add_node(fasta_ids[dnastrs.index(str2)])
      adjacency_list.append(new_SLL)

# write overlapping DNA strands to output
with open('output.txt', 'w') as output_file:
  for item in adjacency_list:
    output_file.write(item.head.val + ' ' + item.head.next.val + '\n')
  

# FIBD: Mortal Fibonacci Rabbits
# Source: https://rosalind.info/problems/fibd/

""" Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

# fills array deliberately in order i.e. dynamic programming
def mortalFib(n, m):
    live_generations = [1, 1]
    for month in range(2, n):
        # adding births
        pop = live_generations[month - 1] + live_generations[month - 2]
        # subtracting deaths
        if month == m:
            pop -= 1
        elif month > m:
            pop -= live_generations[month - m - 1]
        live_generations.append(pop)
    return live_generations[-1]

# parse input and write to output
with open('input.txt', 'r') as input_file:
  data = input_file.readline().split()
  result = mortalFib(int(data[0]), int(data[1]))

with open('output.txt', 'w') as output_file:
  output_file.write(f'{result}')

# memoized fibonacci sequence that was never used whoops
def fib(n, k):
  memo = dict()
  if (n, k) in memo:
    return memo[(n, k)]
  else:
    if (n == 1):
      return 1
    if (n == 2):
      return 1
    else:
      # storing call result in memo for later lookups
      memo[(n, k)] = fib(n - 1, k) + (k * fib(n - 2, k))
      return fib(n - 1, k) + (k * fib(n - 2, k))

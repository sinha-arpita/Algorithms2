#!/usr/bin/python

import sys

def making_change(amount, denominations):
  n=len(denominations)
  table = [[0 for i in range(amount+1)] for j in range(0,n+1)]
  for i in range (1,n+1):
      table[i][0]=1
  for i in range (1,n+1):
     for j in range(1,amount+1):
        if j>=denominations[i-1]:
           table[i][j] = table[i-1][j]+table[i][j-denominations[i-1]]
        else:
           table[i][j]= table[i-1][j]

  print(table)
  return table[n][amount]
print(making_change(10,[1, 5, 10, 25, 50]))
if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]] #array of array result is needed

  result = []
  oneResult= [0]*n # n is the number of players
  generate_rps(oneResult,0, result)# 0 is the index of player number
  return result


def generate_rps(oneResult, playerNumber, result):


    if playerNumber == len(oneResult):#base case (if 4 players arre there then if it reaches 3)2
        print(oneResult)
        result.append(list(oneResult)) #form new list from oneResult before appending otherwise it will be overwritten
        return oneResult

    for item in ("rock","paper","scissors"):
        oneResult[playerNumber] =item
        print(playerNumber,item)
        generate_rps(oneResult,playerNumber+1, result)

print(rock_paper_scissors(2))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
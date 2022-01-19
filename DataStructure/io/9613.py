import sys
import math

input = sys.stdin.readline
t = int(input())

for _ in range(t):
  board = list(map(int, input().split()))
  sum = 0

  for i in range(1, len(board), 1):
    for j in range(i + 1, len(board), 1):
      sum += math.gcd(board[i], board[j])

  print(sum)

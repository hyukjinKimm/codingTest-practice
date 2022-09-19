import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

N = int(input())
p = dict()
for i in range(N):
  word = input()
  p[word] = 1
for i in range(N-1):
  word = input()
  p[word] = 0
for key, val in p.items():
  if val == 1:
    print(key)

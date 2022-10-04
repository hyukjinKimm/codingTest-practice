import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

n = int(input())
d = dict()
for _ in range(n):
  word = input()
  d[word] = d.get(word, 0) + 1
for _ in range(n-1):
  word = input()
  d[word] -= 1
for k, v in d.items():
  if v != 0:
    print(k)
    break
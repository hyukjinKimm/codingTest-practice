import sys
from collections import deque

#sys.stdin=open("input.txt", "r")

N = int(input())
p = dict()
for i in range(N):
  word = input()
  p[word] = p.get(word, 0) + 1 
for i in range(N-1):
  word = input()
  p[word] -= 1 
for k, v in p.items():
  if v == 1:
    print(k)
    break
import sys

sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
N = list(map(int, str(N)))

stack = []

for i in range(len(N)):
  while stack and stack[-1] < N[i] and M > 0:
    stack.pop()
    M -= 1
  stack.append(N[i])
if M > 0:
  for x in stack[:-M]:
    print(x, end = '')
else:
  for x in stack:
    print(x, end = '')

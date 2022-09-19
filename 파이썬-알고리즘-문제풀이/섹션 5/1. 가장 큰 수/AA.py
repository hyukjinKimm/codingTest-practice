import sys
#sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
N = list(map(int, str(N)))
stack = []
for n in N:
  while stack and stack[-1] < n and M > 0:
    stack.pop()
    M -= 1
  stack.append(n)

if M == 0:
  for x in stack:
    print(x, end = '')
else:
  for x in stack[:-M]:
    print(x, end = '')

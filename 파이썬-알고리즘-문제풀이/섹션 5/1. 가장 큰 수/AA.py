import sys
#sys.stdin=open("input.txt", "r")

N ,M = map(str, input().split())
M = int(M)
N = list(map(int, N))

stack = []
for n in N:
 while stack and stack[-1] < n and M > 0:
  stack.pop()
  M -= 1
 stack.append(n)

if M:
  for i in stack[:-M]:
    print(i, end= '')
else:
  for i in stack:
    print(i, end = '')

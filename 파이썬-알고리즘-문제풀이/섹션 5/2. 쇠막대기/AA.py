import sys
#sys.stdin=open("input.txt", "r")

N = input()
stack = []
cnt = 0
for i in range(len(N)):
  if N[i] == '(':
    stack.append('(')
  elif N[i] == ')' and N[i-1] == '(':
    stack.pop()
    cnt += len(stack)
  else:
    stack.pop()
    cnt += 1
print(cnt)


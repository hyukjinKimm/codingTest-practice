import sys
#sys.stdin=open("input.txt", "r")

N = input()
stack = []

cnt = 0
for i in range(len(N)):
  if N[i] == '(':
    stack.append('(')
  elif N[i] == ')':
    stack.pop()
    if N[i-1] == '(':
      cnt += len(stack)
    else:
      cnt += 1 
print(cnt)
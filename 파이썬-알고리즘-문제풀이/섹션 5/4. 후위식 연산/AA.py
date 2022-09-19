import sys
#sys.stdin=open("input.txt", "r")

N = input()
stack = []

cnt = 0
for i in range(len(N)):

  if N[i].isdecimal():
    stack.append(int(N[i]))
  elif N[i] == '*':
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n2*n1)
  elif N[i] == '/':
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n2/n1)
  elif N[i] == '+':
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n2+n1)
  elif N[i] == '-':
    n1 = stack.pop()
    n2 = stack.pop()
    stack.append(n2-n1)
  
print(stack[0])
import sys
#sys.stdin=open("input.txt", "r")

N = input()
stack = []

cnt = 0
for i in range(len(N)):

  if N[i].isdecimal():
    print(N[i], end= '')
  elif N[i] == '(':
    stack.append('(')
  elif N[i] == '*' or N[i] == '/':
    while stack and (stack[-1] == "*" or stack[-1] == '/'):
      print(stack.pop(), end= '')
    stack.append(N[i])
  elif N[i] == '+' or N[i] == '-':
    while stack and stack[-1] != '(':
      print(stack.pop(), end= '')
    stack.append(N[i])
  elif N[i] == ')':
    while stack and stack[-1] != '(':
     print(stack.pop(), end= '')
    stack.pop()
for _ in range(len(stack)):
  print(stack.pop(), end='')
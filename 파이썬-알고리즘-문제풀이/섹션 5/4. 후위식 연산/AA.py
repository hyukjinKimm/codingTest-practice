import sys
from turtle import st
#sys.stdin=open("input.txt", "r")

N = input()
stack = []
for i in range(len(N)):
 if N[i].isdecimal():
  stack.append(int(N[i]))
 else:
  n1 = stack.pop()
  n2 = stack.pop()
  ans = eval(str(n2) + N[i] + str(n1))
  stack.append(ans)
print(stack[0])
import sys
sys.stdin=open("input.txt", "r")


N = int(input())
for i in range(N):
  word = input()
  word = word.upper()
  if word == word[::-1]:
    print("#%d YES" %(i+1))
  else:
    print("#%d NO" %(i+1))  
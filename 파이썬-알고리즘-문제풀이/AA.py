import sys
sys.stdin=open("input.txt", "r")

N = int(input())
for i in range(N):
  word = input()
  word = word.upper()
  for j in range(len(word)//2):
    if word[j] != word[-1-j]:
      print('#%d NO' %(i+1))
      break
  else:
      print('#%d YES' %(i+1)) 


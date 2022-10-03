import sys
sys.stdin=open("input.txt", "r")
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for i in range(k):
  a, b, c = map(int, input().split())
  if b == 0: # 왼쪽으로 회원
    for j in range(c):
      board[a-1].append(board[a-1].pop(0))
  else:
    for j in range(c):
      board[a-1].insert(0, board[a-1].pop()) 
s = 0 
e = n-1
tot = 0
for i in range(n):
  tot += sum(board[i][s:e+1])
  if i < n // 2:
    s += 1
    e -= 1
  else:
    s -= 1
    e += 1
print(tot)

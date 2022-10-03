import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for i in range(n):
  ans = max(ans, sum(board[i]))
  c = 0 
  for j in range(n):
    c += board[j][i]
  ans = max(ans, c)

tmp1 = 0
tmp2 = 0
for i in range(n):
  tmp1 += board[i][i]
  tmp2 += board[i][n-1-i]
ans = max(ans, tmp1, tmp2)
print(ans)
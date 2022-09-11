import sys
#sys.stdin=open("input.txt", "r")

board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0


for i in range(7):
  for j in range(3):
    tmp = board[i][j:j+5]
    if board[i][j:j+5] == tmp[::-1]:
      cnt +=1

    for k in range(2):
      if board[j+k][i] != board[5+j-k-1][i]:
        break
    else:
      cnt += 1
      
print(cnt)
  


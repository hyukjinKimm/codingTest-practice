import sys
#sys.stdin=open("input.txt", "r")

sdoku = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
  ch1 =[0] * 10
  ch2 =[0] * 10
  for j in range(9):
    ch1[sdoku[i][j]] += 1
    ch2[sdoku[j][i]] += 1
  if ch1.count(0) != 1 or ch2.count(0) != 1:
    print('NO')
    break
else:
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      ch1 =[0] * 10
      for k in range(3):
        for m in range(3):
          ch1[sdoku[i+k][j+m]] += 1
    if ch1.count(0) != 1:
      print('NO')
      break
  else:
    print('YES')
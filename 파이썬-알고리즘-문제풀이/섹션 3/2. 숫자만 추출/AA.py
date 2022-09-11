import sys
#sys.stdin=open("input.txt", "r")



word = input()
res = 0
for w in word:
  if w.isdigit():
    res = res*10 + int(w)
cnt = 0
for i  in range(1, res + 1):
  if res % i == 0:
    cnt += 1
print(res)
print(cnt)
import sys
def D(x):
  global cnt
  if x > k:
    for x in res[1:]:
      print(x, end=' ')
    print()
    cnt += 1
  else:
    for i in range(1, n+1):
      if ch[i] == 0:
        ch[i] = 1
        res[x] = i
        D(x+1)
        ch[i] = 0
  

n, k = map(int, input().split())
ch = [0] * (n+1)
res = [0] * (k+1)
cnt=0
def main():
  D(1)
  print(cnt)
  
if __name__ == '__main__':
  main()


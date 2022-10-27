import sys

def D(x, s):
  global cnt
  if s >  k:
    return 
  if x >= cnt:
    return
  if s == k:
    cnt = min(x, cnt)
    
  else:
    for i in range(n):
      D(x+1, s+coin[i])
  

n = map(int, input().split())
coin = list(map(int, input().split()))
k = int(input())
cnt = 1000
def main():
  D(0, 0)
  print(cnt)
  
if __name__ == '__main__':
  main()


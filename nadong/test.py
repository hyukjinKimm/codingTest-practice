import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)


def main():
  n, k = map(int, input().split())
  s = input()
  
  ch = [0] * n
  cnt = 0
  for i in range(n):
    if s[i] == 'P':
      for j in range(max(0, i-k), i):
        if s[j] == 'H' and ch[j] == 0:
          cnt +=1
          ch[j] = 1
          break 
      else:
        for j in range(min(n-1, i+1), i+k+1):
          if j < n and s[j] == 'H' and ch[j] == 0:
            cnt +=1
            ch[j] = 1
            break
  print(cnt)
       


if __name__ == "__main__":
  main()

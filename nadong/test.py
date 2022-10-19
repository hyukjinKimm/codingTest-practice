import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)


def main():
  n, m, k = map(int, input().split())
  candidate = [0] * (n+1)
  for i in range(m):
    genre = input().split()
    for i in range(0, 2*n, 2):
      if candidate[int(genre[i])] < float(genre[i+1]):
        candidate[int(genre[i])] = float(genre[i+1])
  candidate.sort()
  res = 0
  for i in range(k):
    res += candidate[n-i]
  print(round(res, 1))





  
    

if __name__ == "__main__":
  main()

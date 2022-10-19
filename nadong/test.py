

import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)


def main():
  n, m, k = map(int, input().split())
  genre = [[] for _ in range(m)]
  for i in range(m):
    genre[i].append(input().split())
  res = 0 
  s = set()
  while k > 0:
    maxx = 0
    for i in range(m):
      print(i)
      if maxx < float(genre[i][1]):
        if genre[i][0] not in s:
          maxx = float(genre[i][1])
          index = i
    s.add(int(genre[i][0]))
    res += maxx 
    genre[i].pop(0)
    genre[i].pop(0)

    k -= 1
    
    





  
    

if __name__ == "__main__":
  main()

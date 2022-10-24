import sys
import heapq as hq
sys.stdin=open("input.txt", "r")


def main():
  n, m, k = map(int, input().split())
  beer = []
  for _ in range(k):
    beer.append(list(map(int, input().split())))
  beer.sort(key=lambda x:(x[1], -x[0] ))
  print(beer)
  eat = []
  s = 0
  for i in range(k):
    now_alchol = beer[i][1]
    hq.heappush(eat, beer[i][0])
    s += beer[i][0]
    if len(eat) == n:
      if s < m:
        s -= hq.heappop(eat)
      else:
        print(now_alchol)
        return
  else:
    print(-1)

        

  
    

  
   
if __name__ == "__main__":
  main()

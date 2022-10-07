import sys
sys.stdin=open("input.txt", "r")
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
arr.sort()
first = arr[n-1]
second = arr[n-2]


index = 0
sum = 0
xx = m // (k + 1)  # 덩어리가 몇개 나오나 
sum += xx * k * first 
sum += xx * second 
m -= xx*(k+1)
sum += m * first




print(sum) 

  



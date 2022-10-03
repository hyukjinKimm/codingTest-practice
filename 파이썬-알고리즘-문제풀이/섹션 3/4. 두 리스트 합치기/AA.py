import sys
#sys.stdin=open("input.txt", "r")
a = int(input())
arr = list(map(int, input().split()))
b = int(input())
brr = list(map(int, input().split()))

ans = []
i = 0
j = 0
while i < a and j < b:
  if arr[i] < brr[j]:
    ans.append(arr[i])
    i += 1
  else:
    ans.append(brr[j])
    j += 1   
if i == a:
  ans = ans + brr[j:]
else:
  ans = ans + arr[i:]
print(ans)
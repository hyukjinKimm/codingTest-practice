import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
NRR = list(map(int, input().split()))
M = int(input())
MRR = list(map(int, input().split()))

i = 0 
j = 0 
result = []
while i < N and j < M:
  if NRR[i] > MRR[j]:
    result.append(MRR[j])
    j += 1
  else:
    result.append(NRR[i])   
    i += 1 

if i >= N:
  result = result + MRR[j:]
else:
  result = result + NRR[i:]

for x in result:
  print(x, end =  ' ')
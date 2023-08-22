import sys
input= sys.stdin.readline
N, K= map(int, input().split())
lst=[0]*N
for i in range(N):
    lst[i]= int(input())

lst.reverse()
res = 0
for coin in lst:
    res += K//coin
    K= K % coin

print(res)

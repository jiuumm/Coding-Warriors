import sys
input = sys.stdin.readline                            # ****
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum=[0]
tmp = 0

for i in numbers:
    temp = temp+i
    sum.append(temp)              #합배열

for i in range(M):
    s, e = map(int, input.split())
    print(sum[e] - sum[s-1])                #구간합
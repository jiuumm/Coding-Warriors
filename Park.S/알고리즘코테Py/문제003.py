#230728(FRI)
#003. 구간 합 구하기 1 (백준 실버3 11659번)

# 매번 합을 구하면 시간초과! -> 구간합을 이용해야 함
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
array = list(map(int, input().split()))
arraySum = [0]
temp = 0

for i in array:
    temp = temp + i
    arraySum.append(temp)   #합배열 만들기

for i in range(M):
    s,e = map(int,input().split())
    print(arraySum[e] - arraySum[s-1])  #합배열에서 구간합 구하기
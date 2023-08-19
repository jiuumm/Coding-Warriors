#230819(SAT)
#022. 수 정렬하기3(백준 실버5 10989번)

#기수 정렬: 10개의 큐 이용, 시간 복잡도 가장 짧음
import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
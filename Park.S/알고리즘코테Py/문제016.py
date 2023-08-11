#230812(SAT)
#016. 버블 정렬 프로그램1(백준 골드2 1377번)

#N<=500000 이므로 버블정렬 시 시간 초과 -> IDEA)정렬전/후의 index 비교
#sort로 정렬 -> (정렬 전 index - 정렬 후 index)의 최댓값 -> swap 안돼도 반복문 실행되므로 +1

import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()),i))      #데이터, index 순으로 저장

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:    #index 차이 최댓값 저장
        Max = sorted_A[i][1] -i

print(Max+1)
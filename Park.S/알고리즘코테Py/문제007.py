#230801(TUE)
#007. 주몽의 명령(백준 실버4 1940번)
#투포인터 (양 끝에 위치시키고 점점 좁히기)

import sys
input = sys.stdin.readline
N = int(input())    #N의 최대범위가 15000 -> O(nlogn) 사용가능
M = int(input())
A = list(map(int, input().split()))     #N개의 숫자 리스트
A.sort()

count = 0
i = 0
j = N-1

while i<j: #투포인터 이동원칙 따라 포인터 이동하며 처리
    if A[i] + A[j] <M:
        i +=1
    elif A[i] + A[j] >M:
        j -=1
    else:
        count +=1
        i +=1
        j -=1

print(count)

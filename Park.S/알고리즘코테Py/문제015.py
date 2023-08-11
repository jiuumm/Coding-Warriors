#230811(FRI)
#015. 수 정렬하기1 (백준 브론즈1 2750번)

#버블정렬 : 인접 두 데이터 비교, 속도 느림, swap 연산
N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] =temp

for i in range(N):
    print(A[i])
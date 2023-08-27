#BOOK_8
#백준 1253



import sys
input = sys.stdin.readline

N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]                                                 # 찾고자 하는 값
    i = 0                                                       # 포인터 초기화
    j = N-1
    while i<j:
        if A[i]+A[j] == find:
            if i!=k and j!= k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
            elif A[i] + A[j] < find:
                i+= 1
            else:
                j -= 1

print(Result)
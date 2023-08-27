#BOOK_7
#백준 1940
# 정렬 알고리즘의 시간 복잡도: O(nlogn) / 투포인터 알고리즘의 시간 복잡도: O(n)


import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()                                                            #고유번호 오름차순으로 정렬
count = 0
i=0                                                                 #양 끝에 포인터 위치시킴
j=N-1

while i<j:
    if A[i] + A[j] < M:
        i+=1
    elif A[i]+A[j] > M:
        j-=1
    else:
        count += 1
        i += 1
        j -= 1

print(count)
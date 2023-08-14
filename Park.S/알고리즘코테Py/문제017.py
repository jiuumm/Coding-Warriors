#230813(SUN)
#017. 내림차순으로 자릿수 정렬하기(백준 실버5 1427번)

#선택정렬 : (min 찾고 맨앞으로)를 반복 -> 시간복잡도 커서 비효율적
import sys
print = sys.stdout.write
A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max] : # 최댓값 찾기
            Max = j
    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp   #A[i]와 A[Max] swap

for i in range(len(A)):
    print(A[i])
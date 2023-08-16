#230815(TUE)
#018. ATM 인출시간 계산하기(백준 실버3 11399번)

N = int(input())
A = list(map(int, input().split()))
S = [0] *N

for i in range(1,N):
    insertPoint = i
    insertValue = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insertPoint = j+1
            break
        if j == 0:
            insertPoint = 0
    for j in range(i,insertPoint, -1):
        A[j] = A[j-1]
    A[insertPoint] = insertValue

S[0] = A[0]

for i in range(1,N):
    S[i] = S[i-1] + A[i]

sum = 0

for i in range(0,N):
    sum += S[i]

print(sum)
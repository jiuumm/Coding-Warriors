#BOOK_5
#백준 10986



import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
S = [0]*n                                                   #합배열
C = [0]*m                                                   #각 나머지에 해당하는 개수를 저장하는 리스트
S[0] = A[0]

answer = 0                                                  #결과값 초기화

for i in range(1, n):                                       #합 배열 생성
    S[i] = S[i-1] + A[i]


for i in range(n):
    remainder = S[i] % m                                    #합배열을 M으로 나눈 나머지
    if remainder == 0:
        answer += 1                                         #0인 개수만큼 결과 더함(구간이 1인 정답)
    C[remainder] += 1                                       #나머지에 해당하는 인덱스의 값 1 증가


for i in range(m):                                          #C[i]에서 2가지를 뽑는 경우의 수를 정답에 더하기 - 2개의 값이 같아야 하므로 1개 이상인 경우에 실행됨
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)


print(answer)
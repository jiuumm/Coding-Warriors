#230730(SUN)
#005. 나머지 합 구하기 (백준 골드3 10986번)

#구간합 배열을 이용해야 시간초과 안남!
#[IDEA]특정 구간 수들의 나머지연산을 더한 것 == 구간합의 나머지연산
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int, input().split()))
sumArray = [0] * N
count = [0] * M
sumArray[0] = array[0]
answer = 0

for i in range(1,N):        #합배열 저장
    sumArray[i] = sumArray[i-1] + array[i]

for i in range(N):
    remainder = sumArray[i] % M    #합배열 모든 값에 %연산 수행
    if remainder == 0:             #0~i까지의 구간합이 0인 경우 정답
        answer +=1
    count[remainder] +=1           #나머지 같은 인덱스 개수 값 증가

for i in range(M):
    #나머지 같은 인덱스 중 2개 뽑는 경우 정답
    if count[i] > 1:
        answer += (count[i] * (count[i]-1)//2)

print(answer)
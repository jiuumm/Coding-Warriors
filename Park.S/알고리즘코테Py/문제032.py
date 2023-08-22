#230822(TUE)
#032. 동전 개수의 최솟값 구하기(백준 실버3 11074번)
#그리디 : 현재의 상태가 최선이라 가정하는 알고리즘

N, K = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())

count = 0

for i in range(N - 1, -1, -1):
    if A[i] <= K:  # 현재 동전의 가치가 K보다 작거나 같으면 구성에 추가
        count += int(K / A[i])
        K = K % A[i]  # K를 현재 동전을 사용하고 남은 금액으로 갱신

print(count)
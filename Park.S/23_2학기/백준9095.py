#230915(FRI) / 재귀 / 백준9095(실버3)
#점화식 이용 f(n)=f(n-1)+f(n-2)+f(n-3)
#재귀함수인데다가 계산 중복이 많아서 실행시간 비효율적 > DP 추천

def add(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return add(n-1) + add(n-2) + add(n-3)

T = int(input())

for n in range(0,T):
    n = int(input())
    print(add(n))
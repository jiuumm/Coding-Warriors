#백준 10815 숫자카드
import sys

# 입출력 버퍼(입력 빨라짐)
input = sys.stdin.readline

# 카드의 개수 n을 입력
n = int(input())

# 입력받은 카드 숫자 중 중복은 하나로 처리하기 위해 set 사용
nCard = set(map(int, input().split()))

# 비교할 숫자카드 개수 입력
m = int(input())

# 비교할 숫자카드 배열
mCard = list(map(int, input().split()))

# 탐색
for i in range(m):
    if mCard[i] in nCard:
        print(1, end=' ')
    else:
        print(0, end=' ')

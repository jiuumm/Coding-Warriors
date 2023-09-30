#230929(FRI) / 덱 / 실버4
#요세푸스 순열 _그냥 리스트보다 덱을 사용하는게 시간복잡도 더 유리

from collections import deque

def josephus(n, k):
    people = list(range(1, n + 1))   # 초기의 n명 리스트
    result = []                      # 제거된 사람을 담을 리스트

    people = deque(people)  # 리스트를 덱으로 변환

    while people:
        people.rotate(-k + 1)  # 덱을 왼쪽으로 회전하여 k-1만큼 이동
        removed = people.popleft()  # k번째 사람을 제거하고 저장
        result.append(removed)

    return ', '.join(map(str, result))

n, k = map(int, input().split())
answer = josephus(n, k)
print(f"<{answer}>")

from collections import deque

n, k = map(int, input().split())

def josephus_q(n, k):
    res = []
    q = deque()
    for i in range(n):
        q.append(i+1)
    while q:                                            # 큐가 비어있지 않은 동안 반복
        for _ in range(k - 1):
            q.append(q.popleft())                       # k - 1 번째 원소까지는 빼고 다시 큐에 넣음
        res.append(q.popleft())                         # k 번째 원소를 결과에 추가
    result_str = '<' + ', '.join(map(str, res)) + '>'   # ".join(리스트) : 리스트의 각 원소를 문자열로 합쳐서 반환" / "(구분자).join(리스트) : 리스트의 원소 사이에 '구분자'를 넣어서 하나의 문자열로 합쳐줌"
    return result_str


result = josephus_q(n, k)
print(result)





# queue.Queue는 리스트를 기반으로 구현된 큐 -> 리스트를 내부적으로 사용하여 큐의 동작을 시뮬레이트함
# ---> 리스트 내에서 요소를 이동해야 한다. 특히 긴 리스트의 앞부분에서 요소를 제거해야 하는 경우에는 효율적이지 않을 수 있습니다.
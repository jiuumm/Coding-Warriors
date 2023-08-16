from collections import deque                                                   # 파이썬에서는 큐를 deque로 구현
N = int(input())                                                                # 카드의 개수 입력받기
myQueue = deque()                                                               # deque 생성

for i in range(1, N+1):                                                         # 카드의 개수만큼 반복
    myQueue.append(i)                                                           # 큐에 카드 저장
while len(myQueue)>1:                                                           # 큐에 카드가 1장 남을 때까지
    myQueue.popleft()                                                           # 맨위의 카드를 버림
    myQueue.append(myQueue.popleft())                                           # 맨 위의 카드를 가장 아래 카드 밑으로 이동

print(myQueue[0])                                                               # 마지막으로 남은 카드 출력
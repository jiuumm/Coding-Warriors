#230809(WED)
#013. 카드게임(백준 실버4 2164번)

#큐 이용
from collections import deque
N = int(input())
myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)

while len(myQueue) > 1:     #카드가 1장 남을때까지
    myQueue.popleft()       #맨위 카드 버림
    myQueue.append(myQueue.popleft()) #맨위 카드 -> 맨아래로 이동

print(myQueue[0])
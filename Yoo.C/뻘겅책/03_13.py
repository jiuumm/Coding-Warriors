from collections import deque #덱 소환

n= int(input())
myQueue = deque()

for i in range(1, n+1):
    myQueue.append(i)

#카드 1장 남을 때까지 반복
while len(myQueue)>1:
    myQueue.popleft()
    #맨 위 카드 -> 맨 아래 
    myQueue.append(myQueue.popleft())
    
print(myQueue[0])
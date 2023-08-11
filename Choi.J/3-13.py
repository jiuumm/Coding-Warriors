from collections import deque
N=int(input())
myQueue=deque()

for i in range(1, N+1):
    myQueue.append(i)

while len(myQue)>1:
    myQueue.popleft()
    myQueue.append(myQue.popleft())

print(myQueue[0])
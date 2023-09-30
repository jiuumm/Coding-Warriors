from collections import deque
n, k = map(int, input().split())
answer = []
de = deque()
for i in range(1, n+1):
    de.append(i)

while de:
    for i in range(0, k-1):
        de.append(de.popleft())
    answer.append(de.popleft())



print(str(answer).replace('[', '<').replace(']', '>'))
    


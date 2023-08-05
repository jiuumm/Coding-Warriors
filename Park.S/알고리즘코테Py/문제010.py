#230805(SAT)
#010. 최솟값 찾기1(백준 플래티넘 11003번)

from collections import deque
N, L = map(int, input().split())

mydeque = deque()
now = list(map(int, input().split()))

#새로운 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간복잡도 줄임
for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i-L:    #범위 벗어난 값은 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0],end=' ')
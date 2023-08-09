from collections import deque
import sys
input = sys.stdin.readline
#N : 덱의 크기, N: 슬라이딩 윈도우 크기
N,L= map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))
#덱의 구조: (값, 인덱스)
for i in range(N):
    # mydeque[-1][0]은 덱의 마지막 요소의 값을 의미. 이 값이 지금 들어오는 값보다 크면 삭제 (왜?-> 최솟값을 찾는 거니깐!)
    while mydeque and mydeque[-1][0]> now[i]:
        mydeque.pop()
    # 최신으로 들어온 값과 인덱스를 덱에 저장한다.(append 함수 이용)
    mydeque.append((now[i], i)) 
    
    # 만약 덱의 첫번째 요소의 인덱스가 i(현재 인덱스)-L(슬라이딩 윈도우 크기)
    #(현재 인덱스)- (mydeque[0][1])>=L 이면, popleft()
    if mydeque[0][1]<= i-L:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
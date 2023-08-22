from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write

n= int(input())#연산 횟수

myQueue = PriorityQueue()

for i in range(n):
    request = int(input()) #받는 수 
    if request == 0:# 받는 수가 0이면 출력!
        if myQueue.empty(): #큐가 비어있으면 0출력
            print('0\n')
        else: #큐가 비어있지 않으면
            tmp = myQueue.get()#큐가 비어있지 않으면 우선순위로 가져오기
            print(str(tmp[1])+'\n')
    else:
    #최소힙!!
    #받는 수가 0이 아니면 그냥 넣기
    #절댓값 우선 정리 -> 음수 정리
        myQueue.put((abs(request), request))
        
            
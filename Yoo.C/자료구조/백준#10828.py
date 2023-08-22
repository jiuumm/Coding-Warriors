import sys
input= sys.stdin.readline
N= int(input())
stack=[]

#push함수 구현: append 이용
def push(stack, item):
    stack.append(item)
    
#pop함수 구현    
def pop(stack):
    if len(stack)==0: #스택이 비어있는 경우
        print(-1)
    else:
        print(stack[-1])
        stack.pop() # 파이썬 내장함수-> pop이용 
#top 함수 구현    
def top(stack):
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])
    
#size함수 구현
def size(stack):    
    print(len(stack))
    
#empty함수 구현
def empty(stack):
    #스택이 비어 있으면
    if len(stack)==0:
        print(1)
    #스택이 비어 있지 않으면
    else:
        print(0)

for _ in range(N):
    tmp = list(map(str, input().split()))
    if tmp[0]=='push':
        push(stack, tmp[1])
    elif tmp[0]=='top':
        top(stack)
    elif tmp[0]=='size':
        size(stack)
    elif tmp[0]== 'empty':
        empty(stack)
    else:
        pop(stack)
        


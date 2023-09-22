from collections import deque
def solution(progresses, speeds):
    answer = []
    #배포되는 날짜
    de = deque()
    for i in range(len(progresses)):
        remain = 100-progresses[i]
        cnt=0
        while(remain>0):
            remain = remain-speeds[i]
            cnt+=1
        de.append(cnt)
        ####
    if de:
        stack = []
        stack.append(de.popleft())
    #while문 괄호에 de가 아니라 아무것도 안쓰면 안되는 이유

    while(de):
        if stack:
            tmp = de.popleft()
            if tmp <= stack[0]:
                stack.append(tmp)
                
            elif tmp> stack[0]:
                answer.append(len(stack))
                stack.clear()
                stack.append(tmp)
    answer.append(len(stack))            

    return answer

#solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
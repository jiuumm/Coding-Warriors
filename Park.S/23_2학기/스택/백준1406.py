#230922(FRI) / 스택 / 백준1406(실버2)
#일단 스택 문제라니까 스택으로 푸는데... 아이디어 떠올리기 좀 어려웠다.

#IDEA >> 스택 두개 이용, 하나는 커서 왼쪽 문자열 저장/ 하나는 커서 오른쪽

import sys

leftStack = list(sys.stdin.readline().strip())      #커서가 맨뒤이므로 초기 문자열은 leftStack에 저장
rightStack = []
M = int(input())

for _ in range(M):
    edit = sys.stdin.readline().split()
    if edit[0] == 'L' and leftStack:
        rightStack.append(leftStack.pop())         
    elif edit[0] == 'D' and rightStack:
        leftStack.append(rightStack.pop())
    elif edit[0] == 'B' and leftStack:
        leftStack.pop()
    elif edit[0] == 'P':
        leftStack.append(edit[1])                   #입력받은 대로 수행

rightStack.reverse()
leftStack.extend(rightStack)        #rightStack의 문자열을 역순으로 leftStack에 추가

print(''.join(leftStack))

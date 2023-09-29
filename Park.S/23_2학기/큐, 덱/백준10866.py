#230922(FRI) / 덱 / 실버4
#덱

from collections import deque
import sys

# 덱 생성
deque = deque()

# 입력 받기
N = int(input())
for _ in range(N):      # index나 반복횟수를 사용하지 않으면 굳이 i안씀
    command = sys.stdin.readline().strip().split()
    
    if command[0] == 'push_front':
        deque.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        deque.append(int(command[1]))
    elif command[0] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)

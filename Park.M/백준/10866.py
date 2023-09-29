from collections import deque

n = int(input())                                              # 명령의 개수
command = []                                                  # 명령 저장할 배열
my_deque = deque()                                            # 명령을 실행할 큐

for i in range(n):  
    command.append(input())

for com in command:
    if str.isdigit(com):
        if 'b' in com:
            my_deque.append(int(com[-1]))
        else:
            my_deque.appendleft(int(com[-1]))
    else:
        if com == "pop_front":
            if len(my_deque) == 0:
                print("-1")
            else:
                my_deque.popleft()
        elif com == "pop_back":
            if len(my_deque) == 0:
                print("-1")
            else:
                my_deque.pop()
        elif com == "size":
            print(len(my_deque))
        elif com == "empty":
            if len(my_deque) == 0:
                print(1)
            else:
                print(0)
        elif com == "front":
            if len(my_deque) == 0:
                print(-1)
            else:
                print(my_deque[0])
        elif com == "back":
            if len(my_deque) == 0:
                print(-1)
            else:
                print(my_deque[-1])










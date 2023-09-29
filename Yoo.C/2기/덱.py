import sys
input = sys.stdin.readline
from collections import deque
def push_front(x, de):
    de.appendleft(x)
def push_back(x, de):
    de.append(x)
def pop_front(de):
    if de:
        tmp = de.popleft()
        print(tmp)
    else:
        print(-1)
def pop_back(de):
    if de:
        tmp = de.pop()
        print(tmp)
    else:
        print(-1)
def size(de):
    print(len(de))
def empty(de):
    if de:
        print(0)
    else:
        print(1)
def front(de):
    if de:
        print(de[0])
    else:
        print(-1)
def back(de):
    if de:
        print(de[-1])
    else:
        print(-1)

if __name__=='__main__':
    n=  int(input())
    de = deque()
    for _ in range(n):
        
        lst = list(input().split())
        if lst[0]=='push_back':
            push_back(lst[1], de)
        elif lst[0]=='push_front':
            push_front(lst[1], de)
        elif lst[0]== 'front':
            front(de)
        elif lst[0]=='back':
            back(de)
        elif lst[0]== 'size':
            size(de)
        elif lst[0]=='empty':
            empty(de)
        elif lst[0]== 'pop_front':
            pop_front(de)
        elif lst[0]== 'pop_back':
            pop_back(de)

        
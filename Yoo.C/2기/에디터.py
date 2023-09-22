from collections import deque
import sys

input = sys.stdin.readline
s=input().rstrip()
n= int(input())
left= []
for l in s:
    left.append(l)
right=deque()
for _ in range(n):
    order= input().rstrip()
    if order[0]=='L' and left:
       right.appendleft(left.pop())
    elif order[0]=='D' and right:
        left.append(right.pop())
    elif order[0]=='B' and left:
        left.pop()
    elif order[0]=='P':
        left.append(order[2]) 
right_tmp= []
for s in right:
    right_tmp.append(s)

answer = left+right_tmp
for i in answer:
    print(i, end="")

        
        
        

    
import sys
input=sys.stdin.readline

s1=[]
s2=[]
string=input()
for i in string:
    s1.append(i)
    
M=int(input())
for i in range(M):
    com=input()
    if com=='L':
        if s1:
            s2.append(s1.pop())
    elif com=='D':
        if s2:
            s1.append(s2.pop())
    elif com=='B':
        if s1:
            s1.pop()
    elif com=='P':
          s1.append()
          
print()
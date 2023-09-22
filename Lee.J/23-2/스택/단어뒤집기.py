import sys

N=int(input())

for i in range(N):
    n=sys.stdin.readline()
    stack=[]
    for j in n:
        if j==' ':
            while(stack):
                print(stack.pop(), end='')
            print(' ', end='')
        elif j=="\n": 
            while(stack):
                print(stack.pop(), end='')
            print()
        else:
            stack.append(j)
  
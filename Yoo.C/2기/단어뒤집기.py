import sys

t= int(input())
lst = []
for _ in range(t):
    s= input()
    lst.append(s)
for i in range(t):
    
    tmp=lst[i].split(' ')
    for j in range(len(tmp)):
        stack =[]
        for k in range(len(tmp[j])):
            stack.append(tmp[j][k])
            
        for k in range(len(tmp[j])):
            print(stack.pop(), end="")
            #print(stack.pop(), end="")
        if j<len(tmp)-1:
            print(" ", end="")
    print()  
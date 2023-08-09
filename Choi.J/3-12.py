n=int(input())
ans=[0]*n
A=list(map(int, input.split()))
myStack=[]

for i in range(n):
    while myStack and a[myStack[-1]]<A[i]:
        ans[myStack.pop()]=A[i]
    myStack.append(i)
while myStack:
    ans[myStack.pop()]=-1

result=""

for i in range(n):
    result+=str(ans[i])+" "

print(result)
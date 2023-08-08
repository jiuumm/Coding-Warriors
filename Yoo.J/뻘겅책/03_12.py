N= int(input())
A= list(map(int, input().split()))
answer = [0]*N
stack=[]

for i in range(N):
    while stack and A[stack[-1]]>A[i]:#스택에 뭔가가 있을 때
        answer[stack.pop()]=A[i]
    stack.append(i)
    
while stack:
    answer[stack.pop()] = -1

res = ""
for i in range(N):
    res+=str(answer[i])+""

print(res)
        
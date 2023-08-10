n = int(input())
ans = [-1] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

result = ""

for i in range(n):
    result += str(ans[i]) + " "

print(result)

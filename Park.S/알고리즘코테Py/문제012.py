#230808(TUE)
#012. 오큰수 구하기(백준 골드4 17298번)

n = int(input())
ans = [0] *n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    #스택이 차있고, 현재 수열 > 스택top 인덱스가 가리키는 수열 일때
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]   #정답 리스트에 오큰수를 현재 수열로 저장
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ""

for i in range(n):
    result += str(ans[i])+" "

print(result)
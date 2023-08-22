from collections import deque
mydeque = deque()

print(mydeque)
#값, 인덱스
mydeque.append((0,0)) #0번째 인덱스에 값 0 대입
mydeque.append((2,1))
print(mydeque)

print(mydeque[-1][0])


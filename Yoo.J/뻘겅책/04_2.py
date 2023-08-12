import sys
input = sys.stdin.readline

n= int(input()) #배열의 크기
A=[]

for i in range(n):
    A.append((int(input()),i))

Max=0
sorted_A=sorted(A)

for i in range(n):
    if Max<sorted_A[i][1]-i:
        Max = sorted_A[i][1]-i
        
print(Max+1)
    
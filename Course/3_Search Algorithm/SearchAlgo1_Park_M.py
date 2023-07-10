#아직 런타임 에러 발생하지만 고칠예정*
N = int(input())
A = list(map(int, input.split()))
A.sort()
M = int(input())
B = list(map(int, input.split()))

def answer(b):
    pl = 0
    pr = N-1
    
    while pl<=pr:
        pc = (left+right)//2
        if A[pc] == b:
            return True
        if b < A[pc]:
            pr = pc-1
        elif b>A[pc]:
            pl = pc+1
            
for i in range(M):
    if answer(B[i]):
        print(1)
    else:
        print(0)
    
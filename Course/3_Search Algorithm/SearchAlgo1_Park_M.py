#아직 런타임 에러 발생하지만 고칠예정*
N = int(input())
A = list(map(int, input().split()))

A.sort()

M = int(input())
B = list(map(int, input().split()))

for i in range(M):
    pl = 0
    pr = N-1
    found = False

    while pl <= pr:
        pc = (pl+pr)//2
        if A[pc] == B[i]:
            found = True
            break
        elif A[pc] < B[i]:
            pl = pc+1
        else:
            pr = pc-1

    if found:
        print(1)
    else:
        print(0)
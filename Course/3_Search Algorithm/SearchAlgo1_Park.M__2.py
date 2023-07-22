N = int(input())
x = list(map(int, input().split()))

x.sort()

M = int(input())
ky = list(map(int, input().split()))

for i in range (M):
    pl = 0
    pr = N-1
    found = False

    while pl<= pr:
        pc = (pl+pr)//2
        if x[pc] == ky[i]:
            found = True
            break
        elif x[pc] < ky[i]:
            pl = pc+1
        else:
            pr = pc -1
            
    if found:
        print(1, end=' ')
    else:
        print(0, end =' ')
# 백준 1920 숫자카드

def bsearch(ky, a):
     
    pl = 0
    pr = N-1
    
    while pl <= pr:
        pc = (pl + pr) // 2
        if a[pc] < ky:
            pl = pc + 1
        elif a[pc] > ky:
            pr = pc - 1
        else:
            return 1
            
    return 0
            
N = int(input())
a = list(map(int, input().split()))
a.sort()

M = int(input())
b = list(map(int, input().split()))

    
for card_num in b:
    print(bsearch(card_num,a), end=' ')   

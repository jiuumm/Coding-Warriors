import sys
sys.stdin = open("input.txt", "r")
n= int(input())
input= sys.stdin.readline
lst = list(map(int, input().split()))
lst.sort()
res=0
for i in range(n):
    lt=0
    rt=n-1
    cnt=0
    #목표값: lst[i]
    while lt<rt:
        if lst[lt]+lst[rt]<lst[i]:
            lt+=1
        elif lst[lt]+lst[rt]>lst[i]:
            rt-=1
        else:
            #값이 같을 때
            if lt != i and rt != i:
                cnt+=1
                break
            elif lt==i:
                lt+=1
                
            elif rt==i:
                rt-=1
                
    res += cnt       
print(res)

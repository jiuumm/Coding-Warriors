import sys
sys.stdin = open("input.txt", "r")
n= int(input())
m= int(input())
lst = list(map(int, sys.stdin.readline().split()))
#목표값: m : 9
lst.sort()
lt=0
rt=n-1
cnt=0


while lt<rt:
    if lst[lt]+lst[rt]>m:
        rt-=1
        
    elif lst[lt]+lst[rt]==m:
        cnt+=1
        lt+=1
        rt-=1
        
    else:
        lt+=1
        
print(cnt)          

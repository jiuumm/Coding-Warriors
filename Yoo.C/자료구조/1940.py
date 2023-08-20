import sys
sys.stdin = open("input.txt", "r")

n= int(input())
m= int(input())
material = list(map(int, sys.stdin.readline().split()))
material.sort()

cnt=0
lt=0
rt=n-1
#목표값= m
while lt<rt:
    if material[lt]+material[rt]<m:
        lt+=1
    elif material[lt]+material[rt]==m:
        cnt+=1
        rt-=1
        lt+=1
    else:
        rt-=1
print(cnt)

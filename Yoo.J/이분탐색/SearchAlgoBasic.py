import sys
sys.stdin = open("in1.txt", "r")

n,m=map(int, input().split())
a= list(map(int, input().split()))
#n: 자료 갯수, m: 목표값
a.sort()

lt=0
rt=n-1

while lt<=rt:
    mid = (lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]<m:
        lt=mid+1
    else:
        rt=mid-1        
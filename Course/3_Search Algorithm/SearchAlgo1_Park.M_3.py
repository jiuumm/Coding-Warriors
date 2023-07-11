K, N = map(int,input().split())
l = sorted([int(input()) for _ in range(K)])
start, end = 1, sum(l)//N
while start <= end:
    mid = (start+end)//2
    lines = sum([i//mid for i in l])
    if lines >=N:
        start = mid+1
        ans = mid
    else:
        end = mid-1

print(ans)
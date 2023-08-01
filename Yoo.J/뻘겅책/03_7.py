n= int(input())
lt=1
rt=1
sum=1
cnt=0
#목표:n
while lt<=rt:
    if sum<n:
        rt+=1
        sum+=rt
    elif sum==n:
        cnt+=1
        sum-=lt
        lt+=1
    else:
        sum-=lt
        lt+=1
print(cnt)

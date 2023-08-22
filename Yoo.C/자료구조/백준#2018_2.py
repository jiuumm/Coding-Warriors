n= int(input())
lt=1
rt=1
cnt=0
total=0

while True:
    if total<n:
        #처음에 놓친 부분
        if rt<=n:
            total+=rt
            rt+=1
        else:
            break
        
    elif total==n:
        cnt+=1
        total-=lt
        lt+=1
    else:
        total-=lt
        lt+=1
print(cnt)
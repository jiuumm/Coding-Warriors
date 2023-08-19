#시간복잡도 실패


N=int(input())

def check(n):
    cnt=0
    for i in range(1, n+1):
        if n%i==0:
            cnt+=1
    if cnt==2:
        return True     
cnt=0   
for i in range(1, N+1):#i: 1~20
    
    if check(i)==True:
        cnt+=1
        

print(cnt)


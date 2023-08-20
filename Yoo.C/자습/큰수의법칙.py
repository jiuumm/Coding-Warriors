import sys
input= sys.stdin.readline
n, m, k= map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
cnt=0
res=0
first= lst[0] #가장 큰 수
second = lst[1] # 두번째로 큰 수 


while True: #더해지는 횟수가 m이 될 때 까지
    for _ in range(k):
        if cnt>=m:
            break
        else:
            res+=first
            cnt+=1
            
        
        
    if cnt<m:
        res += second
        cnt+=1 
        
    else:
        break
print(res)
       
    
    


N, K= map(int, input().split())
a= []
for i in range(2, N+1):
    a.append(i)


for k in range(len(a)):
    p=a[k]
          
    cnt=0
    #p가 소수인지 검사
    for i in range(1, p+1):
        if p%i==0:
            cnt+=1
        
    if cnt>2:
        break
    #p가 소수라면
    else:
        #배열 a에서 p의 배수들을 제거
        #문제 발생: for문을 돌다가 리스트 크기가 바뀜...
        for j in range(len(a)):
            if a[j]%p==0:
                a.remove(a[j])
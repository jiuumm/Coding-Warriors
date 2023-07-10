#정다면체 문제

n,m= map(int, input().split())

    
lst=[]
for i in range(1, n+1):
    for j in range(1, m+1):
        lst.append(i+j)
#count리스트에 0으로 모두 초기화


count=[]
for i in range(2, n+m+1):
    count.append(0)


for i in range(len(lst)):
    count[lst[i]-2]+=1
res=[]

#최댓값 구하기
max = count[0]

for i in range(1, len(count)):
    if count[i]>=max:
        max = count[i]        
for i in range(1, len(count)):
    if count[i]==max:
        print(i+2, end=' ')
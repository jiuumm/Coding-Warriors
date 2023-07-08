'''
1. N개의 숫자, M이 주어짐.
이분검색으로 M이 정렬된 상태에서 몇 번째에 있는가?
단, 중복값은 존재하지 않는다고 가정.

sol
1. lt, rt 변수를 잡는다.
2. mid = 


*이분탐색은 언제 사용하는가?
-> 결정 알고리즘에서 사용!
특징: 답이 특정범위 안에 있다.

각각 한 개의 랜선의 길이를 최대로 만들어라!

'''


def Count(len):
    cnt=0
    for x in a:
        cnt+=(x//len)
    return cnt

k, n= map(int, input().split())
a=[]
res=0
largest=0
#k개의 길이를 배열 a에 저장
for i in range(k):
    tmp= int(input())
    a.append(tmp)
    largest = max(largest, tmp)
    
#변수 설정
lt=1
rt=largest

#이분탐색 시작!
while lt<=rt:
    #mid= 랜선의 길이
    mid=(lt+rt)//2
    #나눠서 더한 토막의 합이 목표값보다 크거나 같으면 답
    if Count(mid)>=n:
        res=mid
        #그것보다 더 좋은 답이 있는지 탐색
        lt= mid+1
        
    else:
        rt=mid-1
        
print(res)
        


            
    
            
            
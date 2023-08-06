'''
1~N번
i번 사람 걸리는 시간: Pi분

각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값

1. 시간 리스트를 오름차순으로 정렬(선택정렬 이용)
2. 1 2 3 3 4
3. 각 누적합을 구한다.
[1,3,6,9,13]
4. 누적합 리스트에 있는 원소들의 합을 구한다.
32
'''
#N=사람수=timeList의 크기
N= int(input())
time = list(map(int, input().split()))

for i in range(1, N):#i: 1~N-1
    for j in range(i,0,-1):#j: N-1~0, N-2~0, ... 1~0
        if time[j]<time[j-1]: #j가 만약 N-1이라면 j+1일경우 index outof range
            time[j], time[j-1]= time[j-1], time[j]
            
sum_lst = [0]*N
sum_lst[0]= time[0]
#누적합 구하기
for i in range(1, N):
    sum_lst[i]=sum_lst[i-1]+time[i]
       
sum=0
for i in sum_lst:
    sum+=i
    
print(sum) 
 
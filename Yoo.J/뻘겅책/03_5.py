import sys
N, M= map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))
res = 0
sum_lst = [0]*(len(lst))
sum_lst[0]=lst[0]
#나머지 리스트
remainder = [0]*M

for i in range(1,len(lst)):
    sum_lst[i]= sum_lst[i-1]+lst[i]

for i in range(len(sum_lst)):
    sum_lst[i]= sum_lst[i]%M
    if sum_lst[i]%M==0:
        res+=1
    #해당하는 나머지가 곧 remainder 리스트의 인덱스와 같음
    remainder[sum_lst[i]]+=1
for i in range(M):
    if remainder[i]>1:
        res+=remainder[i]*(remainder[i]-1)//2
print(res)
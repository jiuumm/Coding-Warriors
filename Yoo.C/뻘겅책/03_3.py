import sys
input= sys.stdin.readline
n, m= map(int, input().split())
lst_n = list(map(int, input().split()))
lst_sum=[0]
tmp=0
#합배열 만들기
for i in lst_n:
    tmp= tmp+i
    lst_sum.append(tmp)
    

for s in range(m):
     i, j=map(int, input().split())
     print(lst_sum[j]-lst_sum[i-1])
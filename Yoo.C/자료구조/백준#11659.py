
import sys
sys.stdin = open("input.txt", "r")

n, m= map(int, input().split())
#대량의 입력을 처리할 때에는 input()함수보다 
# sys.stdin.readline()이 훨씬 빠르다!
lst_n = list(map(int, sys.stdin.readline().split()))
lst_sum=[0]
tmp=0
#합배열 만들기
for i in lst_n:
    tmp= tmp+i
    lst_sum.append(tmp)
    

for s in range(m):
     i, j=map(int, input().split())
     print(lst_sum[j]-lst_sum[i-1])  
    

